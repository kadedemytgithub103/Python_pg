print("2~20までの整数値を入力してください")
h = int(input("行数:"))
w = int(input("列数:"))

for i in range(h):
    if h<2 or h>20 or w<2 or w>20:
        print("値が正しくありません。")
        break
    for j in range(w):
        print("＊", end="")
    print()