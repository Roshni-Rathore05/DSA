# check Armtstrong number

def checkArmstrong(n):
    #write your code here !!!!!!!!!
    num=n
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**3
        n=n//10

    if num==sum:
        return True
    else:
        return False
