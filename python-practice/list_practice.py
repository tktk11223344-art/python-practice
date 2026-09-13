'''
numbers = [10, 20, 30, 40, 50]

print(numbers[0])#0번째거 출력

for n in numbers:#저장된 값 넘버스에서 하나씩 꺼낸다
    print(n)




amounts = [10000, 25000, 50000, 120000, 30000]
#각 거래 금액을 하나씩 출력
for n in amounts:
    print(n)
#각 거래 금액을 하나씩 출력
for n in amounts:
    if n>=50000:
        print(n)




# 문제: 리스트의 숫자를 하나씩 출력
# numbers 리스트를 만든다: [10, 20, 30, 40, 50]
# for문을 사용해서 숫자를 하나씩 꺼낸다
# 꺼낸 숫자를 출력한다

numbers=[10, 20, 30, 40, 50]

for n in numbers:
    print(n)

    
# 문제: 리스트에서 짝수만 출력하기
# numbers 리스트: [3, 8, 11, 14, 20, 25]
# for문으로 리스트의 숫자를 하나씩 꺼낸다
# 짝수이면 → "짝수"라고 출력한다
# 홀수는 출력하지 않는다

numbers=[3, 8, 11, 14, 20, 25]

for n in numbers:
    if n%2==0:
        print('짝수')
  

# 문제: 50,000원 이상인 거래만 출력
# amounts 리스트: [10000, 75000, 32000, 120000, 45000, 80000]
# for문으로 거래금액을 하나씩 꺼낸다
# 거래금액이 50,000원 이상이면 출력한다
# 50,000원 미만이면 출력하지 않는다

amounts=[10000, 75000, 32000, 120000, 45000, 80000]

for n in amounts:
    if n>=50000:
        print(n)





#리스트의 숫자들을 모두 더하기

amounts=[10000, 20000, 30000, 40000]

total=0

for n in amounts:
    total=total+n

print(total)




#5만원 이상인 것만 합한다

amounts = [10000, 75000, 32000, 120000, 45000, 80000]
total=0
for n in amounts:
    if n>=50000:
        total=total+n

print(total)





# 문제: 50,000원 이상인 거래의 총액 구하기
# amounts = [10000, 75000, 32000, 120000, 45000, 80000]
# total을 0으로 만든다
# for문으로 거래금액을 하나씩 꺼낸다
# 50,000원 이상이면 total에 더한다
# 마지막에 total을 출력한다

amounts = [10000, 75000, 32000, 120000, 45000, 80000]
total=0

for n in amounts:
    if n>=50000:
        total=total+n
print(total)





# 문제: 50,000원 이상인 거래가 몇 개인지 세기
# amounts = [10000, 75000, 32000, 120000, 45000, 80000]
# count를 0으로 만든다
# for문으로 거래금액을 하나씩 꺼낸다
# 50,000원 이상이면 count를 1 증가시킨다
# 마지막에 count를 출력한다

count=0
amounts = [10000, 75000, 32000, 120000, 45000, 80000]

for n in amounts:
    if n>=50000:
        count=count+1

print(count)


#1. 리스트에 추가
numbers = [10, 20, 30] #40을 추가하고 싶다
numbers.append(40)

print(numbers)



#2. 리스트에 삭제
numbers = [10, 20, 30, 40]
numbers.remove(20)

print(numbers)



#3. 뒤죽박죽 정리하고 싶다
numbers = [30, 10, 50, 20, 40]
numbers.sort()
print(numbers)

#4. 리스트 개수 세고 싶다
print(len(numbers))

'''

#1번 위치에 있는 값을 삭제하려면 어떻게 해야 함?

# numbers = [30, 10, 50, 20]
# 1. 40을 리스트에 추가한다
# 2. 10을 삭제한다
# 3. 0번 자리 삭제
# 4. 작은 숫자부터 정렬한다
# 5. 리스트에 숫자가 몇 개 있는지 출력한다

numbers = [30, 10, 50, 20]
numbers.append(40)
numbers.remove(10)
del numbers[0]
numbers.sort()

print(len(numbers))
print(numbers)



