print("税込価格を求めます")
price = int(input("定価"))
tax = int(input("消費税率"))
taxprice = price*tax+price
print("定価 = ",price)
print("税率 = ",tax)
print("税込価格 = ",taxprice)