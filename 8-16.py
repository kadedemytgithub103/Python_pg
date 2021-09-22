dict = {
    "id": "100",
    "name": "大原太郎",
    "age": "19",
}
dict.update(age = "20") #dict["age"] = 20も可
for key,value in dict.items():
    print(key, ":", value, sep="") 