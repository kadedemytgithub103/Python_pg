def judge(list,num):
    if num in list:
        print(num,"は配列に含まれています",sep="")
    else:
        print(num,"は配列に含まれていません",sep="")
num = int(input("整数を入力してください:"))
list = [4,10,59,679,1991,3994,6789,19324]
judge(list,num)