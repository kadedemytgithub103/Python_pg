def add(num1,num2):    
    return num1+num2
def mine(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if num1 != 0 and num2 != 0:
        return num1/num2
    else:
        return 0
def rem(num1,num2):
    if num1 != 0 and num2 != 0:
        return num1%num2
    else:
        return 0
num1 = int(input("整数を入力してください:"))
num2 = int(input("整数を入力してください:"))
print(num1,"+",num2,"=",add(num1,num2),sep="")
print(num1,"-",num2,"=",mine(num1,num2),sep="")
print(num1,"*",num2,"=",mul(num1,num2),sep="")
print(num1,"/",num2,"=",div(num1,num2),sep="")
print(num1,"%",num2,"=",rem(num1,num2),sep="")