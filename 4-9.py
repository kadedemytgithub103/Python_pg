print("0~100までの得点(整数値)を2つ入力してください")
num1 = int(input("1つ目の得点"))
num2 = int(input("2つ目の得点"))
if num1 >= 80 or num2 >= 80:
    print("合格です")
else:
    print("不合格です")