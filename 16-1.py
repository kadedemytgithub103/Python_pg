f = open("16_1_read.txt", "w")

f.write("1\n")
f.write("2\n")
f.write("3\n")
f.write("4\n")
f.write("5\n")


f.close()

f = open("16_1_read.txt")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()
