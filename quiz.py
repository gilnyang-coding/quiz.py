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

#quiz 5 못 품
cnt=0
from random import*
for cus in range(1,51):
    time = randrange(5,51)
    if time<=15:
        print("{0}번째 손님 어서오세요. 소요시간={1}분".format(cus,time))
        cnt+=1
    
    elif time>15:
        print("죄송합니다. 다음에 만납시다.")
print("총 탑승 승객 수:{0}분.".format(cnt))

# quiz 6못 품품
# import sys
# def weight(gender,height):
#     if gender=="남성":
#         return height**2*22
#     elif gender=="여성":
#         return height**2*21
# gender=(input("당신의 성별은?"))
# if gender!="남성" and gender!="여성":
#     print("다시 시도해주세요.")
#     sys.exit()
# height=float(input("키를 알려주세요."))
# weight=round(weight(gender,height/100),2)
# print("당신의 적정 체중은 {0}입니다.".format(weight))

#quiz 7 못 품
# for file in range(1,51):
#     with open("{0}주차.txt".format(file), "w", encoding="utf8") as 보고서:
#         부서=input("당신의 부서는?")
#         이름=input("당신의 이름은?")
#         업무=input("업무를 요약하시오.")
#         보고서.write("이름:{0}\n부서:{1}\n업무 요약:{2}".format(이름, 부서, 업무))

