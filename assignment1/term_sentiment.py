import sys
import json

def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def parse_sentiments(sentiments):
	scores = {}
	for line in sentiments:
		term, score = line.split("\t")
		scores[term] = float(score)
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

def update_scores_for_new_words(text, scores, sentiment):
	for word in text:
		if not word in scores:
			print word
			scores[word] = sentiment
	return scores

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = parse_sentiments(sent_file.readlines())
	tweets = dict_from_json_strings(tweet_file.readlines())
	for tweet in tweets:
		try:
			score_for_tweet = sentiment_score(tweet['text'], scores)
			scores = update_scores_for_new_words(tweet['text'],scores,score_for_tweet)	
		except(KeyError):
			pass
	for word in scores:
		try:
			print '{} {}'.format(word,scores[word])
		except(UnicodeEncodeError):
			pass

if __name__ == '__main__':
	main()
