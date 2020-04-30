# Anil Kumar Ravuru

import spacy
import pandas as pd
import numpy as np

df = pd.read_csv('Final.csv')
reaction_order = ['fb_love', 'fb_haha', 'fb_wow', 'fb_sad', 'fb_angry']
df['top_reaction'] = df['top_reaction'].apply(lambda x: reaction_order.index(x))
print(df['name'].count())

nlp = spacy.load('en_core_web_md')
X = [[] for _ in range(df['name'].count())]
done = 0
for row in df['token_words'].values:
	temp = np.mean(list(map(lambda x: nlp(x).vector, row.split(' ')) ), axis=0)
	# print(temp.shape)
	X[done] = temp
	done+=1
	if done%1000== 0:
		print(done)
X = np.array(X)
# print(X.shape)

pd.DataFrame(X).to_csv("spacy_embeds.csv", header=None, index=None)