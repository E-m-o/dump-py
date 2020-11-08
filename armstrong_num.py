num = input()

def armstrong(num):
    num = int(num)

    sum = 0

    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    
    if num == sum:
       print(num,"is an Armstrong Number")
    else:
       print(num,"is NOT an Armstrong Number")

armstrong(num)
