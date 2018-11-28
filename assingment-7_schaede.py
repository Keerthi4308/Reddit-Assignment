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

#print(posts[:100])

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
#print(top_100)
#print(user['AskReddit'])
#print(top)

# ####Q2
#
# total = 0
# for i in top_100:
#     total += i[1]
# percent = {}
# for i in top_100:
#     percent[i[0]] = i[1]/total

####Q3

top_20 = sort[:20]
top20 = 0
for i in top_20:
    top20 += i[1]
#print(top20/total)

##CR20
from nested_dict import nested_dict
import operator
top_100 = sort[:100]
#print(top_100[:20])
subs = nested_dict(2, int)
top_subs_list = []
for i in top_100:
    top_subs_list.append(i[0])
#print(top_subs_list)

for i in posts:
    subreddit = i['subreddit']
    author = i['author']
    #print(subreddit, author)
    if subreddit in top_subs_list:
        # subs[subreddit] = {}
        #print('yes it is')
        if author == '[deleted]':
            continue
        elif author in subs[subreddit]:
            subs[subreddit][author] += 1
        else:
            subs[subreddit][author] = 1

print("The CR20 for the Top 100 Subreddits are:")
for subreddit in subs:
    subreddit_authors = dict(subs[subreddit])
    #print(subreddit_authors)
    sorted_authors = sorted(subreddit_authors.items(), key=operator.itemgetter(1), reverse=True)
    top_20_auth = sorted_authors[:20]
    top_20_contrib = 0
    total_comm = 0
    for elem in top_20_auth:
        top_20_contrib += elem[1]
#    print("top 20 total:", top_20_contrib)
    for elem in sorted_authors:
        total_comm += elem[1]
#    print("total comments:", total_comm)
    cr20 = top_20_contrib/total_comm
    print(subreddit,":", cr20)