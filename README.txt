Jacopo Caratti
tweetsearch

__________________________________________________________________________________

__________ Startup instructions
__________________________________________________________________________________

SUBMISSION FOLDER: jacopo_caratti_tweetsearch.zip

•	Information about the project: README.txt
•	Collection of tweets: tweets.json.zip
•	Report: tweetsearch_report.pdf
•	Presentation: tweetsearch_presentation.pdf
•	Project folder: tweetsearch
•	Scraper folder: twitter
•	Folder with files discussed in the report: attached
	•	Hashtag-search terms: words.txt
	•	User evaluation results: tweetsearch_data.csv
	•	File to allow CORS policies: web.xml

__________________________________________________________________________________

__________ SETTING Solr
__________________________________________________________________________________

1. Download the solr version 8.6.2 from http://lucene.apache.org/solr.

2. Substitute the solr default web.xml file A with my web.xml file B to allow CORS policies.

•	A = solr-8.6.2/8.6.2/server/solr-webapp/webapp/WEB-INF/web.xml
•	B = jacopo_caratti_tweetsearch/attached/web.xml

3. Run the solr server.

•	cd solr-8.6.2
•	bin/solr start -e cloud

When asked, use default settings and name your collection 'tweets'.

4. Unzip and index the tweets collection jacopo_caratti_tweetsearch/tweets.json.zip.

•	cd solr-8.6.2
•	bin/post -c tweets <relative path to tweets.json file>

5. Open localhost:8983/solr/ on a browser and select the collection tweets. Go to 'schema' and select click on 'Add Copy Field'. Write 'username' as source and '_text_' as destination and click on 'Add CopyField'. Repeat this operation with the same destination '_text_', but first 'full_name' and then 'content' as source.

6. Delete and reindex the tweets collection to apply the schema modifications.

•	cd solr-8.6.2
•	curl -X POST -H 'Content-Type: application/json' --data-binary '{"delete":{"query":"*:*" }}' http://localhost:8983/solr/tweets/update
•	bin/post -c tweets <relative path to tweets.json file>

__________________________________________________________________________________

__________ SETTING Vue.js
__________________________________________________________________________________

1. Install all the packages needed for the frontend and run it:

•	cd jacopo_caratti_tweetsearch/tweetsearch
•	npm install
•	npm run dev

2. At localhost:8080 tweetsearch is now available to you. Good search!

__________________________________________________________________________________

__________ ADDITIONAL NOTES
__________________________________________________________________________________

When creating the submission directory and trying to start the project, I had many problems with npm.
If the steps shown above work, that's fine. Otherwise, download and use the node_modules folder that you find at this Dropbox link: https://www.dropbox.com/sh/lamxsho9jwbyui3/AADKvDA12S2o7W0qgwpOiI_7a?dl=0

If there are still problems, you can directly download my entire already built project at this Dropbox link: https://www.dropbox.com/sh/lamxsho9jwbyui3/AADKvDA12S2o7W0qgwpOiI_7a?dl=0

