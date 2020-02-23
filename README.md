# political-tweets
Scrapes political tweets on key topics for presidential hopefuls using TweetScraper (https://github.com/jonbakerfish/TweetScraper.git) and exports to CSV with fields 'usernameTweet', 'ID', 'text', 'datetime'.
Data can then be analyzed for various trends and/or utilized for model training.


## Setup
From wherever you want to install the directory and run the program:
1. Highly recommend using virtual environments to keep individual projects contained. Use `virtualenv --python=/usr/local/bin/python3 venv` to create virtual environment 'venv'.
2. Activate virtual environment with `source venv/bin/activate` (`deactivate` to exit).
3. Run `git clone https://github.com/jonbakerfish/TweetScraper.git`.
4. `cd TweetScraper` to move into TweetScraper directory.
5. Create '.env' file with `touch .env`.
6. Run the following commands to install requirements and save to requirements file.
- `touch requirements.txt`
- `pip install pandas numpy datetime python-dotenv simplejson scrapy pymongo mysql-connector configparser`
- `pip freeze > requirements.txt`
7. Run the following commands to create necessary subfolders in TweetScraper and move files from `political-tweets` repository to appropriate locations.
- `mkdir src`
- `mkdir inputs`
- `cd ..`
- `cp src/candidate_tweets.py ./TweetScraper/src`
- `cp inputs/issues_terms.json ./TweetScraper/inputs`


## Running the scraper

### How to run:
From the `TweetScraper` directory, run `candidate_tweets.py` with command `./src/candidate_tweets.py`

### What it's doing:
`candidate_tweets.py` scrapes tweets from Twitter handles given specific keywords since a given date.
Uses TweetScraper (`https://github.com/jonbakerfish/TweetScraper`).
Exports as CSV to `TweetScraper/Results` subfolder with fields `'usernameTweet', 'ID', 'text', 'datetime'`.

### More details:
- `keywords` must be dictionary with format {"MainTopic":[list of subtopics as strings]}
- `twitter_handles` must be list of Twitter accounts as strings

Pulls tweets since Jan 01, 2020, unless otherwise specified as 'YYYY-MM-DD'.

If unspecified, twitter_handles will include: `['SenatorBennet','JoeBiden',
'MikeBloomberg','PeteButtigieg','JohnDelaney','TulsiGabbard', 'amyklobuchar',
'DevalPatrick','BernieSanders','TomSteyer', 'ewarren','AndrewYang',
'realDonaldTrump','WalshFreedom','GovBillWeld']`

If unspecified, keywords will include all words in `issues_terms.json`.

The more handles, keywords, and the farther back tweets are pulled, the less complete the pull will bed.
It is recommended to run only a few keywords and only a few handles at a time to get the most complete return.
