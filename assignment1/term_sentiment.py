import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    goodwords = {}
    badwords = {}
    newtermcalc = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary

    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet.keys():
            score=0
            tempwords=[]
            for word in tweet["text"].split():
                stripedword=word.strip('":!@#$%^&*()_+/.,\|?><~`][}{=-').encode('utf-8')
                if stripedword in scores.keys():
                    score += float(scores[stripedword])
                else: tempwords.append(stripedword)
            if score>0:
                for temp in tempwords:
                    if temp in goodwords.keys():
                        goodwords[temp]+=1
                    else:goodwords[temp]=1
            elif score<0:
                for temp in tempwords:
                    if temp in badwords.keys():
                        badwords[temp]+=1
                    else:badwords[temp]=1
    for newterm in goodwords.keys():
        if newterm in badwords.keys():
            if(goodwords[newterm]>0 and badwords[newterm]>0): newtermcalc[newterm] = float(goodwords[newterm] / badwords[newterm])
        else: newtermcalc[newterm] = float(goodwords[newterm])
    for newterm2 in badwords.keys():
        if newterm2 not in goodwords.keys():
            newtermcalc[newterm2] = float(-badwords[newterm2])
    for new in newtermcalc:
         print new, newtermcalc[new]


if __name__ == '__main__':
    main()