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


## noun.py의 댓글별 명사 리스트에서 bigram 형성
bigram=[]
for i in range(len(noun.lists)):
    bgram = bigrams(noun.lists[i])
    bgram_list = [x for x in bgram]
    bigram += bgram_list

## bigram 센 후 빈도로 데이터프레임
bgram_counts = Counter(bigram)
bgram_df = pd.DataFrame({'bgram':bgram_counts.keys(), 'frequency':bgram_counts.values()})
bgram_df.sort_values('frequency', ascending=False, inplace=True)

## 특정 단어가 들어가는 bigram만 뽑아내기
keyword_list = ['영어','수학','문제집','학원','학습지','연산','한글','인강','파닉스','이비에스','밀크티','홈런','스마트올','엘리하이']
for key in keyword_list:
    test_list = []

    for i in range(len(bgram_df)):
        if key in bgram_df.iloc[i,0]:
            test_list.append(True)

        else:
            test_list.append(False)
    bgram_df[key] = test_list

##그래프 그리기
for key in keyword_list:
    twogram_df = bgram_df[bgram_df[key]==True].reset_index()
    twogram_df.drop(columns=['index'],axis=0,inplace=True)
    twogram_df = twogram_df[:110]
    for i in range(len(twogram_df)):
        twogram_df.iloc[i,0] = str(twogram_df.iloc[i,0])
        twogram_df.iloc[i,0] = re.sub('[^ㄱ-힗]','', twogram_df.iloc[i,0])
        twogram_df.iloc[i,0] = re.sub(f'{key}','', twogram_df.iloc[i,0])
    x = [v for v in twogram_df['bgram']]
    y = twogram_df['frequency']
    plt.figure(figsize=(25,13))
    plt.bar(x,y)
    plt.title(f'{key}_bigram',fontsize=40)
    plt.xticks(rotation=90)
    plt.savefig(f'{key}_bigram.png',dpi=300)

plt.show()
