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
				location = None
				# this needs to be looked up to find a state via coordinates
			if tweet['place'] is not None and tweet['place']['country'] == "United States":
				location = tweet['place']['full_name'].replace(' ','').rsplit(',')[-1]
			elif tweet['user']['location'] is not None:
				location = tweet['user']['location']
				location = None
				# the user's location is too variable to use unless we add a lot of parsing rules

			if location is not None and location != "":
				if location not in location_sentiment_collection:
					location_sentiment_collection[location] = []
				location_sentiment_collection[location].append(sentiment_score(tweet['text'],scores))

		except(KeyError):
			pass
		except(UnicodeEncodeError):
			pass
	happiest_state = None
	happiest_state_score = None
	for location, score_list in location_sentiment_collection.iteritems():
		average_sentiment = float(sum(score_list))/float(len(score_list))
		if average_sentiment > happiest_state_score:
			happiest_state = location
			happiest_state_score = average_sentiment

		#print "{} {}".format(location, average_sentiment)

	print happiest_state



if __name__ == '__main__':
	main()
