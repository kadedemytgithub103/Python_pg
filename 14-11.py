address = input("住所を入力してください")
if "市"in address:
    print("市")
elif "群" in address:
    print("群")
else:
    print("東京23区")