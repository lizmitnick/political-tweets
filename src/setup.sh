# !/bin/bash

# From wherever you want to install the directory and run the program:

git clone https://github.com/jonbakerfish/TweetScraper.git
cd TweetScraper
touch .env
virtualenv --python=/usr/local/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
pip install pandas numpy datetime python-dotenv simplejson
pip freeze > requirements.txt
mkdir src
mkdir inputs
cd ..
cp tweet_master.py ./TweetScraper/src
cp issues_terms.json ./TweetScraper/inputs
cd Tweetscraper
