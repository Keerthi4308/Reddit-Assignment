import operator
import collections
cnt = collections.Counter()
import json

####Q1

filename = '/l/research/social-media-mining/public/RC_2015-01-random-sample-1000000.jsonlines'
posts = []
with open(filename) as fh:
    for line in fh:
        line_dict = json.loads(line)
        posts.append(line_dict)

top = {}
user = {}
for i in posts:
    if i['subreddit'] in top:
        user[i['subreddit']] = []
        if i['author'] not in user[i['subreddit']]:
            user[i['subreddit']].append(i['author'])
            top[i['subreddit']] += 1
    else:
        top[i['subreddit']] = 1

sort = sorted(top.items(), key = operator.itemgetter(1), reverse = True)
top_100 = sort[:100]

####Q2

total = 0
for i in top_100:
    total += i[1]
percent = {}
for i in top_100:
    percent[i[0]] = i[1]/total

####Q3

top_20 = sort[:20]
top20 = 0
for i in top_20:
    top20 += i[1]
print(top20/total)

