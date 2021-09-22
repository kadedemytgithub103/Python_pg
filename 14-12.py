address = input("住所を入力してください")
bar = address.index("都").index("道").index("府").index("県")

print(address[bar+1:])