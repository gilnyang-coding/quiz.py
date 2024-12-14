# quiz 2
#풀이 1
from random import*
print("오프라인 스터디 모임 날짜는 매월"+str(int(random()*25+3))+"일로 선정되었습니다") # 문자와 숫자를 같이 쓰려면 str을 꼭 쓰자

#풀이 2
date=randint(4,28)
print(f"오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")

#quiz 3 못 품
#https://naver.com
url="https://naver.com"
url1=url.replace("https://","").replace(".com","") #연속으로도 가능하네??
print(url1)
password= url1[0:3]+str(len(url1))+str(url1.count("e"))+"!"
print(password)
 
 #quiz 4 못 품
users=range(1,21)
print(users)
print(type(users))
users=list(users)
print(users)
shuffle(users)
print(users)
winners=sample(users,4)
print(winners)
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자:{0}".format(winners[1:4])) #어차피 format에서 ,없이 winners[1:4]니까 0번째인 0을 쓴다.
