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


def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = parse_sentiments(sent_file.readlines())
	tweets = dict_from_json_strings(tweet_file.readlines())
	for tweet in tweets:
		print tweet



if __name__ == '__main__':
	main()
