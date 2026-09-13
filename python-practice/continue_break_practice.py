
'''
for n in range(1, 11):     # 1부터 10까지 반복
    if n == 5:             # n이 5라면
        break              # 반복을 완전히 끝낸다
    print(n)               # n을 출력한다


for n in range(1, 11):     # 1부터 10까지 반복
    if n == 5:             # n이 5라면
        continue           # 이번 반복만 건너뛴다
    print(n)               # n을 출력한다


n = 1                    # n에 1을 저장

while n <= 10:           # n이 10 이하인 동안 반복
    if n == 5:           # n이 5라면
        break             # 반복을 완전히 끝낸다
    print(n)             # n을 출력
    n = n + 1             # n을 1 증가



while True:                  # 일단 계속 반복해
    n = int(input("숫자: ")) # 숫자를 입력받는다

    if n == 0:               # 0을 입력했다면
        break                # 반복을 끝낸다

    print(n)                 # 입력한 숫자를 출력한다




#문제:1~10까지 짝수 출력

for n in range(2,11,2):
    print(n)


for n in range(1,11):
    if n%2!=0:
        continue
    print(n)

n=1
while n<=10:
    if n%2==0:
        print(n)
        
    n=n+1
    continue





#문제:1~10까지 홀수 출력

for n in range(1,11,2):
    print(n)



for n in range(1,11):
    if n%2!=0: #홀수라면
        print(n)
    n=n+1    
    continue
    

    
n=1
while n<=10:
    if n%2==0: #짝수라면
        n=n+1  #숫자하나 올리고 잘못왔다
        continue #while로 돌아가서 출력되어라
    
    print(n)
    n=n+1

'''

# while True 사용
# 숫자를 계속 입력받기
# 0을 입력하면 반복 종료
# 짝수이면 "짝수" 출력
# 홀수이면 "홀수" 출력
# 0은 출력하지 않기
# break 사용

while True:
    n=int(input('숫자입력:'))
   
    if n==0:
        break
    elif n%2==0:
        print('짝수')
    else:
        print('홀수')

# while True 사용
# 숫자를 계속 입력받기
# 0을 입력하면 프로그램 종료
# 3의 배수이면 → "3의 배수"
# 3의 배수가 아니면서 짝수이면 → "짝수"
# 둘 다 아니면 → 숫자 출력
# continue 사용
# break 사용

while True:
    n=int(input('숫자:'))

    if n==0:
        break
    
    elif n%3==0:
        print('3의 배수')
        
    elif n%3!=0 and n%2==0:
        print('짝수')
        
    else:
        print(n)
                
