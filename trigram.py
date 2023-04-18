import noun
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import re
from nltk import bigrams
from matplotlib import rc
from matplotlib import font_manager
from nltk.util import ngrams

font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
##noun.py의 댓글별 명사 리스트에서 bigram 형성

trigram=[]
for i in range(len(noun.lists)):
    tgram = ngrams(noun.lists[i],3)
    tgram_list = [x for x in tgram]
    trigram += tgram_list


## trigram 센 후 빈도로 데이터프레임
tgram_counts = Counter(trigram)
tgram_df = pd.DataFrame({'tgram':tgram_counts.keys(), 'frequency':tgram_counts.values()})
tgram_df.sort_values('frequency', ascending=False, inplace=True)
tgram_df1 = tgram_df[:110]

##그래프 그리기
for i in range(len(tgram_df1)):
    tgram_df1.iloc[i,0] = str(tgram_df1.iloc[i,0])
    tgram_df1.iloc[i,0] = re.sub('[^ㄱ-힗]','', tgram_df1.iloc[i,0])
x = [v for v in tgram_df1['tgram']]
y = tgram_df1['frequency']
plt.figure(figsize=(25,13))
plt.bar(x,y)
plt.title('trigram_1',fontsize=40)
plt.xticks(rotation=90)
plt.savefig('trigram_1.png',dpi=300)


tgram_df2 = tgram_df[110:220]
for i in range(len(tgram_df1)):
    tgram_df2.iloc[i,0] = str(tgram_df2.iloc[i,0])
    tgram_df2.iloc[i,0] = re.sub('[^ㄱ-힗]','', tgram_df2.iloc[i,0])
x = [v for v in tgram_df2['tgram']]
y = tgram_df2['frequency']
plt.figure(figsize=(25,13))
plt.bar(x,y)
plt.title('trigram_2',fontsize=40)
plt.xticks(rotation=90)
plt.savefig('trigram_2.png',dpi=300)

plt.show()
