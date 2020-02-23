#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging as log
import os
import pandas as pd
import numpy as np
import datetime as dt
from dotenv import find_dotenv
import json


PROJECT_DIR = find_dotenv().split('.')[0]
INPUT_DIR = os.path.join(PROJECT_DIR, 'inputs')
os.chdir(PROJECT_DIR)

handles = ['SenatorBennet','JoeBiden',
                    'MikeBloomberg','PeteButtigieg',
                    'JohnDelaney','TulsiGabbard',
                    'amyklobuchar','DevalPatrick','BernieSanders',
                    'TomSteyer', 'ewarren','AndrewYang',
            'realDonaldTrump','WalshFreedom','GovBillWeld']

# STEP ONE: read in keywords from `inputs/issues_terms.json`

def read_keywords():
    issues_json = os.path.join(INPUT_DIR, 'issues_terms.json')

    with open(issues_json, "r") as json_file:
        keywords = json.load(json_file) # saves json as dictionary

    return keywords


def get_tweets(topic, since_date='2020-01-01', keywords=read_keywords(),
                                    twitter_handles=handles):
    if os.path.isdir("Data"):
        os.system("rm -R Data") # clear tweets from last query

    # STEP TWO: define queries

    for index2, keyword in enumerate(keywords[topic]):

        for handle in twitter_handles:

            query = '"{}"'.format(str(keyword) + " from:" + str(handle) + " since:" + str(since_date))
            command_qry = "scrapy crawl TweetScraper -a query=" + query

            #  STEP THREE: run queries
            os.system(command_qry)

        if os.path.isdir("Results") is False:
            os.mkdir("Results")

        if os.path.isdir("Data") is False:
            os.mkdir("Data")

        if os.path.isdir("Data/tweet") is False:
            os.mkdir("Data/tweet")

        DATA_DIR = os.path.join(PROJECT_DIR, 'Data')
        TWEET_DIR = os.path.join(DATA_DIR, 'tweet')
        RESULTS_DIR = os.path.join(PROJECT_DIR, 'Results')



        tweets = []
        for file in os.listdir(os.path.join(DATA_DIR, 'tweet/')):
            if file.startswith('.'):
                continue
            with open(os.path.join(TWEET_DIR, file), "r") as tweet_json:
                tweet = json.load(tweet_json)
                tweets.append(tweet)

    return tweets


def tweets_to_csv(since_date='2020-01-01',
                  keywords=read_keywords(),
                  twitter_handles=handles):
    """
    Scrapes tweets from Twitter handles given specific keywords since a given date.
    Uses TweetScraper (`https://github.com/jonbakerfish/TweetScraper`).
    Exports as CSV with fields 'usernameTweet', 'ID', 'text', 'datetime'.

    `keywords` must be dictionary with format {"MainTopic":[<list of subtopics as strings>]}
    `twitter_handles` must be list of Twitter accounts as strings

    Pulls tweets since Jan 01, 2020, unless otherwise specified as 'YYYY-MM-DD'.
    """

    RESULTS_DIR = os.path.join(PROJECT_DIR, 'Results')
    topics = []
    for key, value in keywords.items():
        topics.append(key)

    for index1, topic in enumerate(topics):
        tweets = get_tweets(since_date=since_date,
                            keywords=keywords,
                            topic=topic,
                            twitter_handles=twitter_handles)

        df = pd.DataFrame(tweets, columns=['usernameTweet', 'ID', 'text', 'datetime'])
        df = df.drop_duplicates(subset=['ID'])

        export_name = topic + '.csv'
        export_path = os.path.join(RESULTS_DIR, export_name)
        df.to_csv(export_path, index=False)


        if os.path.isdir("TweetArchive") is False:
            os.mkdir("TweetArchive")

        os.system("cp Data/tweet/* TweetArchive")





def main():
    tweets_to_csv()



if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")
    main()
