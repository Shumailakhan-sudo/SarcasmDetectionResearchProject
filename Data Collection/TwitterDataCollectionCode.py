# Import required libraries
import tweepy
import csv
from credentials import consumer_key, consumer_secret, access_key, access_secret

# Authenticate with Twitter API using the provided keys and access tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Create an API object to interact with the Twitter API
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define the header for the CSV file
header = ['Date', 'username', 'tweet', 'followers_count', 'Location', 'following_counts', 'hashtags']

# Get the search keyword from the user
search_words = input("Enter the Keyword with hash : ")

# Open the CSV file in append mode and create a CSV writer object
csvFile = open(search_words + '.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

# Write the header row to the CSV file
csvWriter.writerow(header)
# Get the number of tweets to search for
numb = int(input('Number of Tweets: '))

# Create a new_search query string to exclude retweets
new_search = search_words + " -filter:retweets"

# Loop through the tweets using the Twitter API search and save relevant data to the CSV file
for tweet in tweepy.Cursor(api.search_tweets, q=new_search, lang="ur", since_id=0, tweet_mode='extended').items(numb):
    # Process the tweet data and write to the CSV file
    csvWriter.writerow([
        tweet.created_at,
        tweet.user.screen_name,
        tweet.full_text.replace('\n', '').encode('utf-8').decode('unicode-escape').encode('latin1').decode('utf-8'),
        tweet.user.followers_count,
        tweet.user.location.encode('utf-8').decode('unicode-escape').encode('latin1').decode('utf-8')
    ])
