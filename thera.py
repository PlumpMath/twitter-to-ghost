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
regex = ' @([a-zA-Z0-9_]{1,15})'
pattern = re.compile(regex)

null = None
out = {
  "meta": {
    "exported_on": 1477990362000,
    "version": "000"
  },
  "data": {
    "tags": [
      {
        "slug": "plato-short",
        "updated_by": 1,
        "meta_description": null,
        "parent_id": null,
        "description": null,
        "name": "plato-short",
        "created_by": 1,
        "created_at": 1477912610000,
        "meta_title": null,
        "id": 1,
        "updated_at": 1477912610000
      },
      {
        "slug": "noise",
        "updated_by": 1,
        "meta_description": null,
        "parent_id": null,
        "description": null,
        "name": "noise",
        "created_by": 1,
        "created_at": 1477912610000,
        "meta_title": null,
        "id": 2,
        "updated_at": 1477912610000
      }

],
    "posts_tags": [],
    "posts": []
  }
}


with open('tweets/tweets.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # skip header
    next(reader)

    for idx, row in enumerate(reader, 1):

        chirp = row[5]

        matches = re.findall(pattern, chirp)
        if matches:
            for match in matches:
                chirp = chirp.replace('@%s' % match, '[%s](https://twitter.com/%s)' % (match, match))

        for tag_id in range(1,3):
            post_tag = {
              "tag_id": tag_id,
              "post_id": idx
            }
            out['data']['posts_tags'].append(post_tag)

        date = 'x'
        time = 'y'
        post = {
          "created_at": 1330072500000,
          "page": 0,
          "updated_at": 1330072500000,
          "created_by": 1,
          "status": "published",
          "markdown": chirp,
          "published_at": 1330072500000,
          "updated_by": 1,
          "id": idx,
          "meta_description": null,
          "slug": "from-programmers-bill-of-rights-2012-all",
          "featured": 0,
          "image": null,
          "html": chirp,
          "published_by": 1,
          "title": "A random thought on %s at %s" % (date, time),
          "author_id": 1,
          "meta_title": null,
          "language": "en_US"
        }
        print('%s: %s' % (idx, chirp))

print(out)
