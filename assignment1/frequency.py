import sys
import json

def dict_from_json_strings(json_list):
	tweets = []
	for json_string in json_list:
		tweets.append(json.loads(json_string))

	return tweets

def update_term_counts(text, term_counts):


def main():
	tweet_file = open(sys.argv[2])
	tweets = dict_from_json_strings(tweet_file.readlines())
	term_counts = {}
	for tweet in tweets:
		term_counts = update_term_counts(tweet['text'], term_counts)
	total_term_count = 0
	for term,count in term_counts.iteritems():
		total_term_count += count
	for term,count in term_counts.iteritems():
		term_freq = float(count)/float(total_term_count)
		print "{} {}".format(term,term_freq)
	
