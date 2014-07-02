__author__ = 'tomi'

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

    #print scores.items() # Print every (

    statelist= {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
    state = {}
    for line in tweet_file:
        tweet = json.loads(line)
        curstate=""
        if "lang" in tweet.keys():
            if tweet["lang"]=="en":
                if ("place" in tweet.keys()) and (tweet["place"] is not None):
                    if "country_code" in tweet["place"]:
                        if tweet['place']['country_code'].lower() == 'us':
                            if tweet['place']['full_name'].split(',')[1].lower()!='us':
                                curstate = tweet['place']['full_name'].split(',')[1]
                else:
                    if "user" in tweet.keys():
                        if "location" in tweet['user']:
                            searchloc = tweet['user']['location'].strip('":!@#$%^&*()_+/.,\|?><~`][}{=-').split()
                            for splited in searchloc:
                                if (splited in statelist.values()):
                                    curstate = splited.upper()
                                elif(splited in statelist.keys()):
                                    curstate = statelist[splited]
        if curstate != "":
            if "text" in tweet.keys():
                score=0
                for word in tweet["text"].split():
                    stripedword=word.strip('":!@#$%^&*()_+/.,\|?><~`][}{=-').encode('utf-8').lower()
                    if stripedword in scores.keys():
                        score += float(scores[stripedword])
                if curstate in state.keys():
                    state[curstate]+=score
                else: state[curstate]=score

    for key, value in sorted(state.items(),key=lambda x: x[1],reverse=True)[:1]:
        print key


if __name__ == '__main__':
    main()

