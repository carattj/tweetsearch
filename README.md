# tweetsearch
A Twitter's Search Engine.

## Report
Here you can find the report and the presentation I made for this project.

## Resources
This directory contains a bunch of files and scripts I used to build and run the search engine.
- tweets.json.zip: collection of tweets
- twitter: directory containing the crawler for Twitter
- words.txt: list of terms I used as hashtags while crawling
- web.xml: configuration file for Solr to allow the CORS policies when making requests to local backend

## tweetsearch
Here is contained the code to run the web application interface.

Install all the packages needed for the frontend and run it:
- npm install
- npm run dev
At localhost:8080 tweetsearch is now available to you. Good search!

Remember: without connecting a backend with an appropriate database of tweets, the search engine won't be operative.

## Run the program
1. Download the solr version 8.6.2 from http://lucene.apache.org/solr.

2. Substitute the solr default web.xml file A with my web.xml file B to allow CORS policies.
- A = solr-8.6.2/8.6.2/server/solr-webapp/webapp/WEB-INF/web.xml
- B = Resources/web.xml

3. Run the solr server.
- cd solr-8.6.2
- bin/solr start -e cloud
When asked, use default settings and name your collection 'tweets'.

4. Unzip and index the tweets collection Resources/tweets.json.zip.
- cd solr-8.6.2
- bin/post -c tweets path_to_tweets.json

5. Open localhost:8983/solr/ on a browser and select the collection tweets. Go to 'schema' and select click on 'Add Copy Field'. Write 'username' as source and '_text_' as destination and click on 'Add CopyField'. Repeat this operation with the same destination '_text_', but first 'full_name' and then 'content' as source.

6. Delete and reindex the tweets collection to apply the schema modifications.
- cd solr-8.6.2
- curl -X POST -H 'Content-Type: application/json' --data-binary '{"delete":{"query":"*:*" }}' http://localhost:8983/solr/tweets/update
- bin/post -c tweets path_to_tweets.json