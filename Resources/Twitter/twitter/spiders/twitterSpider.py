import scrapy
import logging

class HashtagSpider(scrapy.Spider):
    name = 'twittercrawler'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
        'CONCURRENT_REQUESTS': 5, 'DOWNLOAD_DELAY': 0, 'LOG_LEVEL': 'INFO'}
    
    def start_requests(self):
        with open('words.txt', 'r') as f:
            hashtags = f.read().splitlines()
        logging.info(f'{len(hashtags)} hashtags found')
        for hashtag in hashtags:
                search_url = "https://mobile.twitter.com/hashtag/" + hashtag.lower()
                yield scrapy.Request(search_url, callback = self.find_tweets)

    def find_tweets(self, response):
        tweets = response.css('.metadata a::attr(href)').getall()
        logging.info(f'{len(tweets)} tweets found')
        for tweet_id in tweets:
            tweet_id = tweet_id[-23:-4]
            tweet_url = 'https://twitter.com/anyuser/status/' + tweet_id
            yield scrapy.Request(tweet_url, callback = self.parse_tweet)

    def parse_tweet(self, response):
        logging.info('Processing --> ' + response.url)
        username = getUsername(response)
        date = getDate(response)
        emoji = response.css(".TweetTextSize--jumbo .Emoji--forText::attr(alt)").getall()
        content = getContent(response, emoji)
        hashtag, tag = getLinks(content)
        full_name = response.css('.fullname::text').get().strip()
        yield{
            "url": response.url,
            "date": date,
            "full_name": full_name,
            "username": username,
            "profile_pic": response.css(".avatar::attr(src)").get(),
            "content": content,
            "metadata": response.css("div.AdaptiveMedia-container div div img::attr(src)").getall(),
            'hashtag': hashtag,
            'tag': tag,
            "likes": response.css("a.request-favorited-popup strong::text").get(),
            "retweets": response.css("a.request-retweeted-popup strong::text").get(),
            "repost": response.css("div.card2 div.js-macaw-cards-iframe-container::attr(data-card-url)").get(),
            "emoji": emoji
            
        }

def getUsername(tweet):
    s = tweet.css('.tweet .username').get()
    while s.find("<") != -1:
        start = s.find("<")
        end = s.find(">")
        s = s[0: start:] + s[end + 1::]
    s = s[1:end].strip()
    return s

def getDate(date):
    d = date.css("span.metadata span::text").get().split()
    x = d[0].split(":")
    h = int(x[0])
    m = x[1]
    if d[1] == 'PM':
        h = h + 12
    day = d[3]
    mo = d[4]
    y = d[5]
    res = [str(h), m, day, mo, y]
    res = " ".join(res)
    return res

def getContent(tweet, emoji):
    s = tweet.css('.tweet div.js-tweet-text-container p').get()
    counter = 0
    if len(emoji) > 0:
        while s.find('<img class="Emoji Emoji--forText"') != -1:
            start = s.find('<img class="Emoji Emoji--forText"')
            end = len(s) - 1
            for i in range(start,end):
                if s[i] == '>':
                    s = s[0: start:] + " " + emoji[counter] + " " + s[i + 1::]
                    counter += 1
                    break
    while s.find("<") != -1:
        start = s.find("<")
        end = s.find(">")
        s = s[0: start:] + s[end + 1::]
    if s.find("pic.twitter.com/") != -1:
        start = s.find("pic.twitter.com/")
        end = len(s) - 1
        s = s[0: start:] + s[end + 1::]
    return s.strip()

def getLinks(content):
    content = content.split()
    hashtag = []
    tag = []
    for i in content:
        if i[0] == "#":
            hashtag.append(i)
        elif i[0] == "@":
            tag.append(i)
    return hashtag, tag