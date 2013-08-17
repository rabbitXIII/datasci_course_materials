import sys
import json

def dict_from_json_strings(json_list):
	tweets = []
	for json_string in json_list:
		tweets.append(json.loads(json_string))

	return tweets

def main():
	tweet_file = open(sys.argv[1])
	tweets = dict_from_json_strings(tweet_file.readlines())


if __name__ == '__main__':
	main()
