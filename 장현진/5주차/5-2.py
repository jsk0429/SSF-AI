a=int(input("숫자를 입력하세요:"))#숫자를 사용자에게 입력받아 a에 할당하기
for i in range(1,a+1):
    print(" "*(a-i)+"* "*i)#1에서 a까지 반복하여 공백을 a-i만큼 곱한뒤 print(공백을 a에서 하나씩 줄어들고 별은 하나씩 늘어나 피라미드 구조를 형성함.)
