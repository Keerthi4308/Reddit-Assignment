import operator
import collections
cnt = collections.Counter()
import json
import pandas as pd

####Q1 : top100 subreddit with unique users

inputfile = '/l/research/social-media-mining/public/RC_2015-01-random-sample-1000000.jsonlines'
outputfile="reddit-statistics.csv"
posts = []
with open(inputfile) as fh:
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
#print (top_100)

top_100_dict = { i[0] : i[1]  for i in top_100 }
#print (top_100_dict)

dt=pd.DataFrame.from_dict(top_100_dict, orient='index', columns=['top_100'])
#print(dt)
dt.to_csv(outputfile, sep='\t')

####Q2 %content for each subreddit in top100

content = {}
total=0
for i in posts:
    if i['subreddit'] in top_100_dict:
        if i['subreddit'] in content:
                content[i['subreddit']]+=1
        else:
                content[i['subreddit']] = 1
        total+=1

for key,value in content.items():
    value=value/total
    content[key]=value

dt=pd.DataFrame.from_dict(content, orient='index', columns=['content_percent'])
#print(dt)
dt.to_csv(outputfile, sep='\t', mode='a')

#print (content)

# ####Q3 #comments/comment+submission (not mandatory)

# top_20 = sort[:20]
# top20 = 0
# for i in top_20:
#     top20 += i[1]
# print(top20/total)

