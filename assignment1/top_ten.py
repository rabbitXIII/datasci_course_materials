import sys
import json
import operator

def dict_from_json_strings(json_list):
	tweets = []
	for json_string in json_list:
		tweets.append(json.loads(json_string))

	return tweets

def main():
	tweet_file = open(sys.argv[1])
	tweets = dict_from_json_strings(tweet_file.readlines())
	hashtag_counts = {}
	for tweet in tweets:
		try:
			hashtags = tweet['entities']['hashtags']
			for hashtag in hashtags:
				if hashtag['text'] not in hashtag_counts:	
					hashtag_counts[hashtag['text']] = 0
				hashtag_counts[hashtag['text']] += 1
		except(KeyError):
			pass
	sorted_hashtag_list = sorted(hashtag_counts.iteritems(), key=operator.itemgetter(1))
	# sorts the counts in increasing order
	sorted_hashtag_list.reverse()

	for i in range(10):
		print "{} {}".format(sorted_hashtag_list[i][0], float(sorted_hashtag_list[i][1]))

if __name__ == '__main__':
	main()
