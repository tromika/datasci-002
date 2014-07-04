__author__ = 'tomi'

import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #afinnfile = open("AFINN-111.txt")
    #    scores = {} # initialize an empty dictionary
    #    for line in sent_file:
    #        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    #        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    hashtaglist = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if "entities" in tweet.keys():
            if "hashtags" in tweet['entities']:
                for tag in tweet['entities']['hashtags']:
                    #print tag['text']#tweet['entities']['hashtags'][tag]['text']
                    if tag['text'] in hashtaglist.keys():
                        hashtaglist[tag['text']]+=1
                    else: hashtaglist[tag['text']] = 1

    for key, value in sorted(hashtaglist.items(),key=lambda x: x[1],reverse=True)[:10]:
        print key, value


if __name__ == '__main__':
    main()

