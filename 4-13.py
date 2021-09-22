num = int(input("0~100までの得点(整数値)を入力してください"))
if num == 100:
    print("満点合格です")
elif num < 100 and num >= 60:
    print("合格です")
else :
    print("不合格です")