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

def update_scores_for_new_words(text, scores, new_scores, sentiment):
	for term in text.replace('\n','').replace('.','').replace(',','').rsplit(' '):
		if not term in scores and term != "":
			if not term in new_scores:
				new_scores[term] = []
			new_scores[term].append(sentiment)
	return new_scores

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = parse_sentiments(sent_file.readlines())
	tweets = dict_from_json_strings(tweet_file.readlines())
	new_scores = {}
	for tweet in tweets:
		try:
			score_for_tweet = sentiment_score(tweet['text'], scores)
			new_scores = update_scores_for_new_words(tweet['text'],scores,new_scores,score_for_tweet)	
		except(KeyError):
			pass
	for term,score_list in new_scores.iteritems():
		average_score = float(sum(score_list))/float(len(score_list))
		try:
			print '{} {}'.format(term,average_score)
		except(UnicodeEncodeError):
			pass

if __name__ == '__main__':
	main()
