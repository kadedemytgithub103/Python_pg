f = open("16_2_read.txt", "w")

f.write("名前:Tanaka, 年齢:18\n")
f.write("名前:Sato, 年齢:20\n")
f.write("名前:Suzuki, 年齢:25\n")

f.close()

f = open("16-2.txt")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()