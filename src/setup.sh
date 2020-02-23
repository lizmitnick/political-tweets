# !/bin/bash

# From wherever you want to install the directory and run the program:


virtualenv --python=/usr/local/bin/python3 venv
source venv/bin/activate
git clone https://github.com/jonbakerfish/TweetScraper.git
cd TweetScraper
touch .env
pip install -r requirements.txt
pip install pandas numpy datetime python-dotenv simplejson scrapy pymongo mysql-connector configparser
pip freeze > requirements.txt
mkdir src
mkdir inputs
cd ..
cp src/candidate_tweets.py ./TweetScraper/src
cp inputs/issues_terms.json ./TweetScraper/inputs
cd Tweetscraper
