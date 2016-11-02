import csv
import sys

"""
headers:
0 tweet_id
1 in_reply_to_status_id
2 in_reply_to_user_id
3 timestamp
4 source
5 text
6 retweeted_status_id
7 retweeted_status_user_id
8 retweeted_status_timestamp
9 expanded_urls
"""

with open('tweets/tweets.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # skip header
    next(reader)

    for row in reader:

        if row[1] and row[2]:
            #print('BOTH %s' % row[5])
            pass
        else:
            print('BOTH %s' % row[5])
            #print('<skipping>')


        #sys.exit()
