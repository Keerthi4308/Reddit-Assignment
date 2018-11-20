import json
filename= '/l/research/social-media-mining/public/RC_2015-01-random-sample-1000000.jsonlines'
posts=[]
with open(filename) as fh:
	for line in fh:
	    line_dict=json.loads(line)
	    posts.append(line_dict)
print (posts[:1])

