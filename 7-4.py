a = 1
b = 1
while a <= 100000:
    a += b
    b += 1

#合算した後にnに+1しているのでn-1する
print("100000を超えるnの数は",b-1,"です。")