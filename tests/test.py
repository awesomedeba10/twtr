import os, sys
import pandas as pd

project_path = os.path.abspath(os.getcwd())

if project_path not in sys.path:
    sys.path.append(project_path)

from twtr.ProcessTweet import ProcessTweet

df = pd.read_csv(project_path + '\data\Tweets.csv')

tweet = ProcessTweet()

df['processed_text'] = df['text'].apply(tweet.preprocess)
df['lemmatized_text'] = df['processed_text'].apply(lambda x: tweet.standardize(x, return_type='list'))

print(df[['text', 'processed_text', 'lemmatized_text']])





