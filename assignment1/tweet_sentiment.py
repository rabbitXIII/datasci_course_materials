import sys
import json

def lines(fp):
	print str(len(fp.readlines()))

def parse_sentiments(sentiments):
	scores = {}
	for line in sentiments:
		term, score = line.split("\t")
		scores[term] = int(score)
	return scores

def dict_from_json_strings(json_list):
	tweets = []
	for json_string in json_list:
		tweets.append(json.loads(json_string))

	return tweets

def sentiment_score(text, scores):
	score = 0
	for word in text.split():
		if scores.has_key(word): score += scores[word]
	return score

def print_sentiment_scores_for_tweets(tweets, scores):
	for tweet in tweets:
		try:
			print sentiment_score(tweet['text'], scores)
		except(KeyError):
			pass

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = parse_sentiments(sent_file.readlines())
	tweets = dict_from_json_strings(tweet_file.readlines())
	print_sentiment_scores_for_tweets(tweets, scores)

if __name__ == '__main__':
	main()
