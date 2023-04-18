import noun
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
from wordcloud import WordCloud

## 폰트 한글 설정, 경로 변경 필요
font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

noun_counts = Counter(noun.words)
df_freq = pd.DataFrame({'word':noun_counts.keys(),'frequency':noun_counts.values()}).set_index('word')

top_nouns = dict(noun_counts.most_common(800))

## 수동으로 주제에 따라 분류....
df_company = df_freq.loc[['밀크티','홈런','엘리하이','윙크','스마트올','씽크빅','빨간펜','이비에스','구몬','공부방','엠베스트','엄마표','온리원','눈높이','아이캔두','하프스터디','팩토','연필영어','밀크티아이','어학원','윤','리딩게이트','쿠키','도요새','천재교육','비상'],:]
df_company.loc['온리원','frequency']=df_company.loc['온리원','frequency']+df_freq.loc['와이즈','frequency'] ## 와이즈캠프가 온리원으로 이름 변경
df_company.loc['엘리하이','frequency']=df_company.loc['엘리하이','frequency']+df_freq.loc['엘리','frequency']
df_company.loc['윙크','frequency']=df_company.loc['윙크','frequency']+df_freq.loc['윙','frequency']


df_age = df_freq.loc[['미취학','유아','유치원','4살','5살','6살','7살','초1','초2','초3','초4','초5','초6','중1','중2','중3','저학년','고학년','초등','중등','중학생'],:]
df_age.loc['저학년','frequency']=df_age.loc['저학년','frequency']+df_freq.loc['초저','frequency']
df_age.loc['중등','frequency']=df_age.loc['중등','frequency']+df_freq.loc['중학','frequency']
df_age.loc['초등','frequency']=df_age.loc['초등','frequency']+df_freq.loc['초등학생','frequency']

df_subject = df_freq.loc[['영어','수학','과학','한글','국어','독서','사회','피아노','한국사','축구','역사','한자','미술','태권도','예체능','코딩','수영','운동','줄넘기'],:]
df_subject.loc['수학','frequency']=df_subject.loc['수학','frequency']+df_freq.loc['영수','frequency']
df_subject.loc['영어','frequency']=df_subject.loc['영어','frequency']+df_freq.loc['영수','frequency']+df_freq.loc['국영','frequency']
df_subject.loc['국어','frequency']=df_subject.loc['국어','frequency']+df_freq.loc['국영','frequency']
df_subject.loc['태권도','frequency']=df_subject.loc['태권도','frequency']+df_freq.loc['태권','frequency']
df_subject.loc['한국사','frequency']=df_subject.loc['한국사','frequency']+df_freq.loc['국사','frequency']


df_paper=df_freq.loc[['최상위','개념','심화','응용','사고력','기본','원리','만점왕','디딤돌','실력','우등생','수박씨','오투','우공비','큐브','1031','혼공','해법','기탄'],:]

df_contents=df_freq.loc[['연산','파닉스','리딩','논술','독해','게임','개뼈','문법','도서관','이야기','만화','실험','특강','동영상','원서','도서','원어민','발음','스피킹','놀이','북클럽'],:]

df_interest=df_freq.loc[['수업','문제집','책','선생','학습지','문제','화상','강의','학교','교재','인강','컨텐츠','지면','교과서','영상','교과연계','연계','유튜브','교과'],:]
df_interest.loc['선생','frequency']=df_interest.loc['선생','frequency']+df_freq.loc['쌤','frequency']++df_freq.loc['강사','frequency']
df_interest.loc['컨텐츠','frequency']=df_interest.loc['컨텐츠','frequency']+df_freq.loc['콘텐츠','frequency']
df_interest.loc['유튜브','frequency']=df_interest.loc['유튜브','frequency']+df_freq.loc['유투','frequency']
df_interest.loc['교과','frequency']=df_interest.loc['교과','frequency']+df_freq.loc['교과목','frequency']
df_interest.loc['문제집','frequency']=df_interest.loc['문제집','frequency']+df_freq.loc['문제지','frequency']

## 경쟁사, 학생 나이, 과목, 교재, 콘텐츠, 기타 관심사에 따른 빈출어 그래프
df_list = [df_company, df_age, df_subject, df_paper, df_contents, df_interest]
titles = ['경쟁사','학생의 나이','과목','교재','콘텐츠','기타 관심사']

## 한 그림 안에 뽑기
#rows = [0,0,0,1,1,1]
#columns=[0,1,2,0,1,2]

#fig,ax=plt.subplots(2,3,figsize=(30,15))
#for df, row, column, title in zip(df_list,rows,columns,titles):
#    df.plot(kind='bar', ax=ax[row,column], title=title)
#    ax[row,column].get_legend().remove()
#    ax[row,column].set_xticks(ax[row,column].get_xticks())
#    ax[row,column].set_xticklabels(ax[row,column].get_xticklabels(), rotation=45, ha='right')

for df,title in zip(df_list,titles):
    df.plot(figsize=(25,13),kind='bar',legend=None)
    plt.xticks(fontsize=15,rotation=45)
    plt.title(title, fontsize=30)
    plt.xlabel(None)
    plt.savefig(f'{title}_bar.png',dpi=300)

#plt.figure(figsize=(30,15))
#for df, num, title in zip(df_list,range(6),titles):
#    wordcloud=WordCloud(background_color="white",random_state=42,font_path='NanumBarunGothic.ttf',width=1600, height=500).generate_from_frequencies(df['frequency'].to_dict())
#    plt.subplot(3,2,num+1)
#    plt.imshow(wordcloud)
#    plt.title(title)
#    plt.axis("off")
#plt.savefig('worldcloud.png',dpi=300)

for df,title in zip(df_list,titles):
    wordcloud=WordCloud(background_color="white",random_state=142,font_path='NanumBarunGothic.ttf',width = 3000, height = 1000).generate_from_frequencies(df['frequency'].to_dict())
    plt.figure(figsize=(25,13))
    plt.imshow(wordcloud)
    plt.title(title, fontsize=40)
    plt.axis("off")
    plt.savefig(f'{title}_wc.png',dpi=300)

if __name__ == "__main__":
	print('단어 언급 횟수의 분포 상황',df_freq.describe())
	print('\n','언급 횟수 상위 800 단어','\n',top_nouns)
	plt.show()
