# Author:ZYM
import copy
names = ["zhangsan","lisi","zhangyimin","mazi"]

# print(names[1:3])#切片操作
# print(names[-1])#切片操作
# print(names[-3:-1])
# print(names[-2:])

name2 = copy.deepcopy(names)


for i in  names:
    print(i)
print(names[::2])
names.append("zhangyimin")

print(names)

names.insert(1,"luochunlei")

# print(names)

names[2] = "zhangerwa"

# print(names)

#delete

# names.remove("zhangsan")
# del names[1]
names.pop(1)

# print(names)

# print(names.index("mazi"))

# print(names.count("zhangyimin"))

# names.clear()
names.reverse()

names.sort()
# print(names)

