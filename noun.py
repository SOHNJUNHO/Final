import pandas as pd
from collections import Counter
from konlpy.tag import Mecab

m=Mecab()

df = pd.read_csv('data.csv')
df.drop_duplicates(['comment'],inplace=True)
df.dropna(subset=['comment'], axis=0, inplace=True)

#아이캔두
df['comment']=df['comment'].str.replace(pat=r'켄',repl='캔',regex=True)
df['comment']=df['comment'].str.replace(pat=r'아이캔\*',repl='아이캔두',regex=True)
df['comment']=df['comment'].str.replace(pat=r'아이ㅋㄷ',repl='아이캔두',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅇㅇㅋㄷ',repl='아이캔두',regex=True)
df['comment']=df['comment'].str.replace(pat=r'아이캔ㄷ',repl='아이캔두',regex=True)
df['comment']=df['comment'].str.replace(pat=r'아이\*두',repl='아이캔두',regex=True)
df['comment']=df['comment'].str.replace(pat=r'아\*ㅋㄷ',repl='아이캔두',regex=True)
df['comment']=df['comment'].str.replace(pat=r'아이\*\*',repl='아이캔두',regex=True)
df['comment']=df['comment'].str.replace(pat=r'아\*\*두',repl='아이캔두',regex=True)

#밀크티
df['comment']=df['comment'].str.replace(pat=r'밀크T',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀크t',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀ㅋ티',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀크ㅌ',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀ㅋㅌ',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅁㅋ티',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅁㅋㅌ',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀\*티',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀크\*',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀\*\*',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀크@',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀@티',repl='밀크티',regex=True)
df['comment']=df['comment'].str.replace(pat=r'밀@@',repl='밀크티',regex=True)

#밀크티아이
df['comment']=df['comment'].str.replace(pat=r'밀크티 아이',repl='밀크티아이',regex=True)


#엘리하이
df['comment']=df['comment'].str.replace(pat=r'앨',repl='엘',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘ㄹ',repl='엘리',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘@',repl='엘리',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘\*',repl='엘리',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘리ㅎㅇ',repl='엘리하이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘리하ㅇ',repl='엘리하이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘리하\*',repl='엘리하이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘리하@',repl='엘리하이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅇㄹㅎㅇ',repl='엘리하이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘리\*\*',repl='엘리하이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘리@@',repl='엘리하이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘\*\*이',repl='엘리하이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엘\*\*\*',repl='엘리하이',regex=True)

#윙크
df['comment']=df['comment'].str.replace(pat=r'윙\*',repl='윙크',regex=True)
df['comment']=df['comment'].str.replace(pat=r'윙ㅋ',repl='윙크',regex=True)
df['comment']=df['comment'].str.replace(pat=r'0ㅋ',repl='윙크',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅇㅋ',repl='윙크',regex=True)
df['comment']=df['comment'].str.replace(pat=r'윙@',repl='윙크',regex=True)
df['comment']=df['comment'].str.replace(pat=r'윙크\s?스쿨',repl='윙크',regex=True)

#엘,엠,젤
df['comment']=df['comment'].str.replace(pat=r'앰',repl='엠',regex=True)
df['comment']=df['comment'].str.replace(pat=r'잴',repl='젤',regex=True)

#엠베스트
df['comment']=df['comment'].str.replace(pat=r'엠베',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠\*스트',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠베\*트',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠베스\*',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠\*\*\*',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠베\*\*',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠\*\*트',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠베@트',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠베스ㅌ',repl='엠베스트',regex=True)
df['comment']=df['comment'].str.replace(pat=r'엠ㅂㅅㅌ',repl='엠ㅂㅅ트',regex=True)

#눈높이
df['comment']=df['comment'].str.replace(pat=r'눈높\*',repl='눈높이',regex=True)
df['comment']=df['comment'].str.replace(pat=r'눈높@',repl='눈높이',regex=True)

#빨간펜
df['comment']=df['comment'].str.replace(pat=r'팬',repl='펜',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅃㄱㅍ',repl='빨간펜',regex=True)
df['comment']=df['comment'].str.replace(pat=r'빨간ㅍ',repl='빨간펜',regex=True)
df['comment']=df['comment'].str.replace(pat=r'빨\*펜',repl='빨간펜',regex=True)
df['comment']=df['comment'].str.replace(pat=r'빨간\*',repl='빨간펜',regex=True)
df['comment']=df['comment'].str.replace(pat=r'빨간@',repl='빨간펜',regex=True)
df['comment']=df['comment'].str.replace(pat=r'빨@펜',repl='빨간펜',regex=True)

#이비에스
df['comment']=df['comment'].str.replace(pat=r'ebs',repl='이비에스',regex=True)

#온리원
df['comment']=df['comment'].str.replace(pat=r'온\*원',repl='온리원',regex=True)
df['comment']=df['comment'].str.replace(pat=r'온니원',repl='온리원',regex=True)

#홈런
df['comment']=df['comment'].str.replace(pat=r'ㅎㄹ',repl='홈런',regex=True)
df['comment']=df['comment'].str.replace(pat=r'홈ㄹ',repl='홈런',regex=True)
df['comment']=df['comment'].str.replace(pat=r'홈@',repl='홈런',regex=True)
df['comment']=df['comment'].str.replace(pat=r'홈\ㄹ',repl='홈런',regex=True)
df['comment']=df['comment'].str.replace(pat=r'\*런',repl='홈런',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅇㅇㅅㅋㄹ',repl='아이스크림',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅇㅇ스크림',repl='아이스크림',regex=True)
df['comment']=df['comment'].str.replace(pat=r'아이스크림\s?홈런',repl='홈런',regex=True)

#와이즈캠프
df['comment']=df['comment'].str.replace(pat=r'ㅇㅇㅈㅋㅍ',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와\*\*\*\*',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와캠',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와\*',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와ㅋ',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와@',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와ㅇㅈㅋㅍ',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와이즈ㅋㅍ',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와이즈\*\*',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와이즈@@',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와이즈캠\*',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와이즈캠@',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와이즈캠프',repl='와이즈',regex=True)
df['comment']=df['comment'].str.replace(pat=r'와이즈캠ㅍ',repl='와이즈',regex=True)

#웅진
df['comment']=df['comment'].str.replace(pat=r'ㅇㅈ',repl='웅진',regex=True)
df['comment']=df['comment'].str.replace(pat=r'웅ㅈ',repl='웅진',regex=True)
df['comment']=df['comment'].str.replace(pat=r'웅\*',repl='웅진',regex=True)
df['comment']=df['comment'].str.replace(pat=r'웅@',repl='웅진',regex=True)

#씽크빅
df['comment']=df['comment'].str.replace(pat=r'ㅆㅋㅂ',repl='ㅆㅋㅂ',regex=True)
df['comment']=df['comment'].str.replace(pat=r'씽ㅋ빅',repl='씽크빅',regex=True)
df['comment']=df['comment'].str.replace(pat=r'씽ㅋㅂ',repl='씽크빅',regex=True)
df['comment']=df['comment'].str.replace(pat=r'씽\*\*',repl='씽크빅',regex=True)
df['comment']=df['comment'].str.replace(pat=r'씽\*빅',repl='씽크빅',regex=True)
df['comment']=df['comment'].str.replace(pat=r'씽@빅',repl='씽크빅',regex=True)
df['comment']=df['comment'].str.replace(pat=r'싱크빅',repl='씽크빅',regex=True)
df['comment']=df['comment'].str.replace(pat=r'씽크\*',repl='씽크빅',regex=True)
df['comment']=df['comment'].str.replace(pat=r'웅진\s?씽크빅',repl='씽크빅',regex=True)
df['comment']=df['comment'].str.replace(pat=r'웅진 북클럽',repl='웅진북클럽',regex=True)

#스마트올
df['comment']=df['comment'].str.replace(pat=r'스\*마올',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'스\*\*올',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅅㅁㅌㅇ',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'ㅅㅁㅌ올',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'스마트ㅇ',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'스마트\*',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'스마트@',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'스마@올',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'스마\*올',repl='스마트올',regex=True)
df['comment']=df['comment'].str.replace(pat=r'웅진\s?스마트올',repl='스마트올',regex=True)

##나이
df['comment']=df['comment'].str.replace(pat=r'8(세|살)',repl='초1',regex=True)
df['comment']=df['comment'].str.replace(pat=r'9(세|살)',repl='초2',regex=True)
df['comment']=df['comment'].str.replace(pat=r'10(세|살)',repl='초3',regex=True)
df['comment']=df['comment'].str.replace(pat=r'4세',repl='4살',regex=True)
df['comment']=df['comment'].str.replace(pat=r'5세',repl='5살',regex=True)
df['comment']=df['comment'].str.replace(pat=r'6세',repl='6살',regex=True)
df['comment']=df['comment'].str.replace(pat=r'7세',repl='7살',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(초|초등|초등학교)\s?1',repl='초1',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(초|초등|초등학교)\s?2',repl='초2',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(초|초등|초등학교)\s?3',repl='초3',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(초|초등|초등학교)\s?4',repl='초4',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(초|초등|초등학교)\s?5',repl='초5',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(초|초등|초등학교)\s?6',repl='초6',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(중|중등|중학교)\s?1',repl='중1',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(중|중등|중학교)\s?2',repl='중2',regex=True)
df['comment']=df['comment'].str.replace(pat=r'(중|중등|중학교)\s?3',repl='중3',regex=True)
df['comment']=df['comment'].str.replace(pat=r'초딩',repl='초등',regex=True)
df['comment']=df['comment'].str.replace(pat=r'유딩',repl='유치원',regex=True)
df['comment']=df['comment'].str.replace(pat=r'중딩',repl='중학생',regex=True)

## 추가...
df['comment']=df['comment'].str.replace(pat=r'(AI|ai|Ai)',repl='인공지능',regex=True)
df['comment']=df['comment'].str.replace(pat=r'인공 지능',repl='인공지능',regex=True)
df['comment']=df['comment'].str.replace(pat=r'영ㅇ',repl='영어',regex=True)
df['comment']=df['comment'].str.replace(pat=r'영\*',repl='영어',regex=True)
df['comment']=df['comment'].str.replace(pat=r'교과 연계',repl='교과연계',regex=True)
df['comment']=df['comment'].str.replace(pat=r'연필 영어',repl='연필영어',regex=True)

stopwords = ['무료','체험','거','저','저희','것','감사','게','때','패드','년','맘','애','고민','생각','원','제','듯','만',
'쪽지','비교','정보','댓글','이번','부분','걸로','챗','저흰','답변','말씀','건가요','느낌','얼마','요즘','지금','센터','아들','딸','올해','안녕','그게','사용',
'오늘','진행','학모','연락처','중요','때문','일','전','둘','번','데','개','건','하나','둘','등','달','월','가지','후','걸','꺼','곳','해요','첨','결국','명',
'외','경우','쪽','뭐','내년','땐','그거','날','이거','동안','테','어디','쥴','사','이게','사랑','다음','채팅','무엇','그때','적','당','뒤','거기','문의','여기',
'이','나','반','편','대','안','건데','눈','문','회','그건','인','법','위','중','넵','주','점','기','건지','이것','그것','개월','주세요','주일','결제','수','학습','시간','군데',
'정도','엄마','분','가능','도움','필요','활용','학기','학년','하루','시','부탁','권','우리','자기','내','공부','추가','끝','장','등등','조금','나름','등록','줄','답글',
'대신','아무것','ㄱ','무료','체험','나중','이건','뭔가','텐데','뭘','대부분','이후','브','만큼','대로','그날','언니','님','뿐','ㄷ','걸까요','그걸로','그걸','최근','이젠','댓','살','글','첫째','둘째']

words = []
for i in range(len(df)):
    for word in (m.nouns(df.iloc[i,0])):
        if word not in stopwords:
           words.append(word)

noun_counts = Counter(words)
noun_freq = pd.DataFrame({'noun':noun_counts.keys(),'frequency':noun_counts.values()}).set_index('noun')
top_nouns = dict(noun_counts.most_common(800))

lists=[]
for i in range(len(df)):
    nouns=[]
    for word in (m.nouns(df.iloc[i,0])):
        if word not in stopwords:
            nouns.append(word)
    if len(nouns)!=0:
        lists.append(nouns)

if __name__ == "__main__":
    print(top_nouns)
    print(len(df))
    print(words[:10])
    print(lists[:10])
    print(len(words))
    print(len(lists))
    print(noun_freq.describe())
