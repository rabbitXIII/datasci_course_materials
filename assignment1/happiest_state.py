import sys
import json

def dict_from_json_strings(json_list):
	tweets = []
	for json_string in json_list:
		tweets.append(json.loads(json_string))

	return tweets

def parse_sentiments(sentiments):
	scores = {}
	for line in sentiments:
		term, score = line.split("\t")
		scores[term] = float(score)
	return scores

def sentiment_score(text, scores):
	score = 0
	for word in text.split():
		if scores.has_key(word): score += scores[word]
	return score

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = parse_sentiments(sent_file.readlines())
	tweets = dict_from_json_strings(tweet_file.readlines())
	location_sentiment_collection = {}
	for tweet in tweets:
		location = None
		try:
			if tweet['coordinates'] is not None:
				location = tweet['coordinates']
				# this needs to be looked up to find a state
			if tweet['place'] is not None:
				location = tweet['place']['fullname']
			elif tweet['user']['location'] is not None:
				location = tweet['user']['location']

			if location is not None and location != "":
				print location
				if location not in location_sentiment_collection:
					location_sentiment_collection[location] = []
				location_sentiment_collection[location].append(sentiment_score(tweet['text'],scores))
				print location_sentiment_collection[location]

		except(KeyError):
			pass



if __name__ == '__main__':
	main()
