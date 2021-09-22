print("0~100までの値(整数値)を2つ入力してください")
num1 = int(input("1つ目の値"))
num2 = int(input("2つ目の値"))
if num1 == num2 :
    print("同じ値です")
elif num1 > num2:
    print("値が大きいのは",num1,"です。")
else:
    print("値が大きいのは",num2,"です。")