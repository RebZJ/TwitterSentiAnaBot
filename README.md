# TwitterSentiAnaBot

Just a little twitter sentiment analysis tool

##Important
Add a file called "Auth.txt" to hold you twitter credenditials, should look something like this:

Replace X with your twitter creds:

{"consumer_key":"XXXXXXXXX",
"consumer_secret":"XXXXXXXXXXXXX",
"access_token":"XXXXXXXXXXXXXXXXXXXXX",
"access_token_secret":"XXXXXXXXXXXXXXXXXXXXXXXX"}

##Useage
Just use the function senti_analysis(user, number) and use the @ of the user for the user field, and the number is the tweet you want e.g 0 is the latest tweet, 1 is second latest etc.

Example: print(senti_analysis("@elonmusk", 0))
Prints Elon's Musks latest tweet

#Score
The score has 4 fields that are pretty self explanatory:
*Negative
*Neutral
*Positive
*Compound: A combination of all of the above accounted into one

Written in python processing data using NLTK and sentimentent analysis ML model called Vader


