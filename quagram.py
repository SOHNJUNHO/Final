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

quagram=[]
for i in range(len(noun.lists)):
    qgram = ngrams(noun.lists[i],4)
    qgram_list = [x for x in qgram]
    quagram += qgram_list


## trigram 센 후 빈도로 데이터프레임
qgram_counts = Counter(quagram)
qgram_df = pd.DataFrame({'qgram':qgram_counts.keys(), 'frequency':qgram_counts.values()})
qgram_df.sort_values('frequency', ascending=False, inplace=True)
qgram_df = qgram_df[:50]

##그래프 그리기
for i in range(len(qgram_df)):
    qgram_df.iloc[i,0] = str(qgram_df.iloc[i,0])
    qgram_df.iloc[i,0] = re.sub('[^ㄱ-힗]','', qgram_df.iloc[i,0])
x = [v for v in qgram_df['qgram']]
y = qgram_df['frequency']
plt.figure(figsize=(25,13))
plt.bar(x,y)
plt.title('quagram',fontsize=40)
plt.xticks(rotation=90)
plt.savefig('quagram.png',dpi=300)

plt.show()
