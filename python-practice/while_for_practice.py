'''
while 조건:
    반복할 코드



n=3
while n>0:  #while n !=0:
    print(n)
    n=n-1
    



n=5
while n>0: #양수인 것만 반복하겠다
    if n%2 ==0: #n을 2로 나눈 나머지가 0이라면
        print(n) #n을 출력하시오
    n=n-1




n = 1

while n < 10: #n이 10보다 작다면 다음걸로 ㄱㄱ
    print(n)
    n = n + 2




n=1
while n<6:
    print(n)
    n=n+1

n=10
while n>0:
    print(n)
    n=n-1


n=2
while n<=10:
    if n%2==0:
        print(n)
    n=n+1

-------------------------------------

# range(1,6)에는 1,2,3,4,5가 들어있음
# range(5)에는 0,1,2,3,4
# range(1, 10, 2)에는 1~19까지 2씩 증가
# range(10,5,-1)에는 10~6까지 감소

for n in range(1,6): #랜지 1~6에서 하나 꺼내서 n에 넣어반복
    print(n)


for n in range(1, 6):  # 1부터 5까지 반복
    if n % 2 == 0:     # n이 짝수인지 확인
        print(n)       # 짝수라면 출력


for n in range(1,11): #1~10까지 랜지 중에
    if n%2==0 #n이 짝수라면
    print(n) #n을 출력



#문제:1부터 5까지 출력 while, for in range


n=1
while n<=5:
    print(n)
    n=n+1

for n in range(1,6):
    print(n)






#문제 : 1부터 10까지 중 3의 배수를 찾기

#for in풀기
for n in range(1,11):#랜지 안에 있는 것들을 하나씩 가져오기
    if n% 3==0:
        print(n)

#while로 풀기
n=1
while n<=10:#n이 10이하인 동안 반복
    if n%3==0:
        print(n)
    n=n+1





#문제 : 1부터 10까지의 숫자 중 홀수만 더한 결과

#for in풀기
total=0

for n in range(1,11):
    if n%2!=0:
        total=total+n

print(total)



#while로 풀기    
total=0 #합계를 저장할 상자 total, 처음은 0넣기
n=1 #n이라고 이름붙여진 상자에 1 넣기

while n<=10: #n이 10이하인 동안 반독
    if n%2!=0: #만약 홀수라면
        total=total+n #토탈이라는 상자에 n을 더할게
    n=n+1

print(total) #토탈 상자를 추출





# 문제:1부터 10까지의 숫자 중 짝수만 모두 더하기

#for in풀기
total=0
for n in range(1,11):
    if n%2==0:
        total=total+n
print(total)


#while로 풀기
total=0 #여기서 0은 숫자임, 문자는 "10"
n=1

while n<=10:
    if n%2==0: #n=5는 저장,n==5는 n이 5와 같은가?
        total=total+n
    n=n+1

print(total)


'''


#문제:1부터 20까지 숫자 분석하기
#for문 1~20
#3의 배수면 "3의 배수"
#3의 배수가 아니면서(안해도됨) 짝수이면 "짝수"
#둘 다 아니면 숫자를 출력

for n in range(1,21):
    if n%3==0:
        print('3의 배수')
    elif n%2==0:
        print('짝수')
    else:
        print(n)

n=1
while n<=20:
     if n%3==0:
        print('3의 배수')
    elif n%2==0:
        print('짝수')
    else:
        print(n)
    n=n+1 #while은 for와 달리 자동으로 숫자 안넘어감


#문제: 1부터 20까지 숫자 분석하기
# for문 1~20
# 3의 배수:"3의 배수" 
# 3의 배수가 아니면서 짝수:"짝수"
# 둘 다 아니면 숫자 출력

for n in range(1,21):
    if n%3==0:
        print('3의 배수')
    elif n%2==0:
        print('짝수')
    else:
        print(n)
