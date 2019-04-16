import tweepy
from nltk.tokenize import word_tokenize
import json
from nltk.corpus import stopwords
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


consumer_key = 'fJvo5SeYGf83ZBVMVotJ5BfiC'
consumer_secret = '64pj8JkLhMRZbqhQRxKuKzzH0ob1qEETMH6Kk0hpSHBVSdp1Nn'
access_token = '1101670693656125440-8UrXC2geQBmpDCrzQ3iaTqYheJLc2Y'
access_token_secret = 'XgKeiRPXN0Fg7H6kwlGTfjXvl2zEA2SaAhUsEI4OOQ4fA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

analyser = SentimentIntensityAnalyzer()

api = tweepy.API(auth)

public_tweets = api.user_timeline("@elonmusk",count=2)

#this is an array
tokenized_sentence = (word_tokenize(public_tweets[1].text))
words_to_filter = []

stop_words=set(stopwords.words("english"))

def strip_words(text_array, words_to_strip):
	filtered_sentence = []
	for w in text_array:
		if w not in words_to_strip:
			filtered_sentence.append(w)
	return filtered_sentence

new_tokenized_sentence = strip_words(tokenized_sentence, stop_words)

def sentiment_analyser_scores(sentence):
	score = analyser.polarity_scores(sentence)
	print("{} {}".format(sentence,str(score)))

sentiment_analyser_scores(public_tweets[1].text)