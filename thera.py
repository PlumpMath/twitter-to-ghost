import csv
import sys
import re

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

# from http://stackoverflow.com/a/11361109/51280
regex = '@([a-zA-Z0-9_]{1,15})'
pattern = re.compile(regex)

def replacer(string, before, after):
    string = string.replace(before, after)

with open('tweets/tweets.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # skip header
    next(reader)

    for row in reader:
        chirp = row[5]

        matches = re.findall(pattern, chirp)
        if matches:
            for match in matches:
                chirp = chirp.replace('@%s' % match, '[%s](https://twitter.com/%s)' % (match, match))
        print(chirp)
