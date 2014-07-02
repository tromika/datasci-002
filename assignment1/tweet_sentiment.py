import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary

    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet.keys():
            score=0
            for word in tweet["text"].split():
                stripedword=word.strip('":!@#$%^&*()_+/.,\|?><~`][}{=-').encode('utf-8').lower()
                if stripedword in scores.keys():
                    score += float(scores[stripedword])
            print score
        else: print 0


if __name__ == '__main__':
    main()