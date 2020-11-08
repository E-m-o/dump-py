num = input()

def fact(num):
    try:
        num = int(num)
        if num<0:
            return 'Positive integer input only'
        if num==0:
            return 'Not possible or Undefined'
        if num==1:
            return 1
        else:
            return num*fact(num-1)
    except:
        return 'Positive integer input only'
    
    
print(fact(num))