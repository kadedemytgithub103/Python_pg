x = []
y = []
for i in range(10):
    s = int(input("整数を入力してください"))
    if s%2 == 0:
        x.append(s)
    else:
        y.append(s)
print("偶数地配列 = ",x)
print("奇数地配列 = ",y)