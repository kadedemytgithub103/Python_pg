sum = 0
start = int(input("開始数:"))
end = int(input("終了数:"))

for num in range(start,end+1):
    sum += num
print("合計:",sum,sep="")