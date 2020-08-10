import tweepy
from nltk.tokenize import word_tokenize
import json
from nltk.corpus import stopwords
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def senti_analysis(user, number):
	# read the file in for authentication
	with open('Auth.txt') as json_file:
		data = json.load(json_file)
		consumer_key = data["consumer_key"]
		consumer_secret = data["consumer_secret"]
		access_token = data["access_token"]
		access_token_secret = data["access_token_secret"]

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	analyser = SentimentIntensityAnalyzer()

	api = tweepy.API(auth)

	public_tweets = api.user_timeline(user, count=number+1)

	# this is an array
	tokenized_sentence = (word_tokenize(public_tweets[number].text))
	words_to_filter = []

	stop_words = set(stopwords.words("english"))


	def strip_words(text_array, words_to_strip):
		filtered_sentence = []
		for w in text_array:
			if w not in words_to_strip:
				filtered_sentence.append(w)
		return filtered_sentence


	new_tokenized_sentence = strip_words(tokenized_sentence, stop_words)


	def sentiment_analyser_scores(sentence):
		score = analyser.polarity_scores(sentence)
		print("{} {}".format(sentence, str(score)))

	return {"score": analyser.polarity_scores(public_tweets[number].text),
        "tweet": public_tweets[number].text,
        "user": user}


#print(senti_analysis("@elonmusk", 0))

