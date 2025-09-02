#CHAPTER ONE
#DATA types

# name = "shankar"
# age = 23
# salary = 10000.10
# age2 = age
# print(name)
# print(age)
# print("my name is:",name)
# print("my age is:",age)
# print("my salary:",salary)
# print(age2)
# print(type(age))
# print(type(name))
# print(type(salary))
# age = 43
# old = False
# a =  None
# print(type(a))
# print(type(old))

#Arithmetic Operators

# a = 5
# b = 10
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)

#Relational Operators

# a = 50
# b = 20
# print( a == b)
# print( a != b)
# print( a > b)
# print( a < b)

#assignment Operators

# num = 10
# num += 10
# num -= 10
# num *= 10
# num /= 10
# num %= 10
# num **= 10
# print("num:",num)

#logical Operators

# a = 50
# b = 20
# print( not False)
# print(not (a>b))
# val1 = True
# val2 = False
# print("Logical Operator:",val1 and val2)
# print("Logical Operator:", (a == b) or (a > b))

#Type Conversion

# a = int("2")
# b = 40.5
# print(type(a))
# print( a + b)

#input statement
# name = input("enter your name:")
# print("Wel come",name)
# name = float(input("enter your name:"))
# print(type(name),name)

#practice questions

# a = int(input("enter first no:"))
# b = int(input("enter second no:"))
# print("sum of two no:",a + b)

# side = float(input("enter one side"))
# print("square=", side * side)

# a = float(input("enter one side"))
# b = float(input("enter one side"))
# print("avg=",(a*b)/2)

# a = int(input("1="))
# b = int(input("2="))
# print(a>=b)

#CHAPTER TWO

# str1 = "this is python program \niam learning"
# print(str1)

# a = "shankar"
# b = "gouda"
# full_name = a + b
# print(full_name)

# str1 ="jwvjewcwjejmwjr9wm"
# len1 = len(str1)
# print(len1)

# final = a + " " + b
# print(final)
# print(len(final))

# print(a[4:7])
#print(a[-4:-7])

# str1 = "iam studying python"
# print(str1.endswith("av"))

# str1 = "iam studying python"
# print(str1.capitalize())
# print(str1.replace("y","u")) #find count
# print(str1.count("python"))

#practice questions

# name = input("enter your name: ")
# print(len(name))

# st = "$$$$$$$$$$$$$$"
# print(st.count("$"))

#Conditional Statements

# age = 17
# if(age >=18):
#     print("eligible to vote")
# elif(age<=18):
#     print("not eligible")

# l = "blue"
# if(l=="green"):
#     print("go")
# elif(l=="red"):
#     print("stop")
# else:
#     print("no light")

# marks = int(input("enter marks:"))
# if(marks>=90):
#     print("A")
# elif(marks>=80 and marks<=90):
#     print("B")
# elif(marks>=70 and marks<=80):
#     print("C")
# else:
#     print("D")    

# num = int(input("enter number:"))
# rem = num % 2
# if(rem==0):
#     print("even")
# else:
#     print("odd")

# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = int(input("enter a number"))
# if(a>=b and a>=c):
#     print("1")
# elif(b>=c):
#     print("2")
# else:
#     print("3")

# a = int(input("enter a number"))
# if(a % 7 == 0):
#     print("multi")
# else:
#     print("no multi")

#CHAPTER THREE

#Lists

# m = [12,25,225,255,6,98,15]
# print(m)
# print(len(m))
# print(m[0])
# print(m[3])

# student = ["shankar",99.5, 85, "bsc"]
# print(student)
# student[0]="gouda"
# print(student)
# print(student[0:3])

# list = [1,9,3]
# list.append(4)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse
# print(list)
# list.insert(1, 5)
# print(list)
# list.remove(1)
# print(list)
# list.pop(3)
# print(list)

# tup = (1,5,8,6,6,6,7)
# print(type(tup))
# print(tup)
# print(tup.index(7))
# print(tup.count(6))

#practice questions

# movie = []
# list1 = input("enter first movie:")
# list2 = input("enter second movie:")
# list3 = input("enter third movie:")

# movie.append(list1)
# movie.append(list2)
# movie.append(list3)
# print(movie)

# li = [1,2,3,2,1,]
# copy_list1 = li.copy()
# copy_list1.reverse()
# if(copy_list1==li):
#     print("palindrome")
# else:
#     print("not palidrome")

# grade = ("c","d","a","a","b","b","b","a")
# print(grade.count("a"))

# grade = ["c","d","a","a","b","b","b","a"]
# grade.sort()
# print(grade)

#CHAPTER 4

# info = {    #dict
#     "name":"shankar",
#     "age":22,
#     "topic":"coding",
#     "from":"apna college",
#     22.5:22.6,
#     "nsn" : [20220110]
# }
# print(info)
# print(info["name"])
# info["name"]="gouda"
# info["code"]="vs"
# print(info)

# std = {
#     "name":"shankar","subjects":{
#     "phy":97,
#     "chem":65,
#     "cs":98
# }
# }
# print(std["subjects"])
# print(std["name"])
# print(len(list(std.keys())))
# print(list(std.values()))
# print(std.items())
# pairs = list(std.items())
# print(pairs[0])
# print(std.get("name"))
# std.update({'city':'bangalore'})
# print(std)

# col = {1,1,2,3,5,"shankar","gouda"}  #sets
# print(len(col))
# print(type(col))

# col = set()
# col.add(1)
# col.add(2)
# col.add(3)
# col.remove(1)
# col.add((1,4,8,6))
# col.clear()
# # col.pop()
# print(col)
# print(len(col))

# set1 = {1,2,3,4}
# set2 = {4,5,6}
# str = set.union(set1,set2)
# str = set.intersection(set1,set2)
# print(str)

#practice

# dict = {"table":["a piece of furniture","list of facts and figures"],"cat":"a small animal"}
# print(dict)

# classroom = {"python","java","c++","js","java","c","python","c++"}
# print(len(classroom))

# student ={}
# x = int(input("enter phy:"))
# student.update({"phy":x})

# x = int(input("enter math:"))
# student.update({"math":x})

# x = int(input("enter cs:"))
# student.update({"cs":x})

# print(student)

# std = {(int,9.0),(float,9)}
# print(std)

#Chapter 5
#loops

# count = 1
# while count <=5:
#     print("my name")
#     count += 1
# print(count)

# j = 1
# while j<=100:
#     print("ur name",j)
#     j +=1
# print(j)

# i = 5
# while i>=1:
#     print(i)
#     i -= 1

# i = 1
# while i <=100:
#     print(i)
#     i +=1

# i = 100
# while i >=1:
#     print(i)
#     i -=1

# i =  int(input('enter a number:'))
# n = 1
# while n <=10:
#     print(i*n)
#     n+=1

# i = int (input("enter:"))
# n = 1
# while n <=10:
#     print(n**i)
#     n += 1

# n = [1,2,8,7,6,8,9,47]
# i = 0
# while i < len(n):
#     print(n[i])
#     i += 1

# n = (1,2,8,7,6,8,9,47)
# x = 7
# i = 0
# while i < len(n):
#     if(n[i]==x):
#         print("found",i)
#         break
#     else:
#         print("finding")
#     i += 1

# i = 1
# while i <= 5:
#     print(i)
#     if(i==3):
#         break
#     i += 1

# i =  1
# while i<= 5:
#     if(i==3):
#         i += 1
#         continue
#     print(i)
#     i += 1

# i =  1
# while i<= 10:
#     if(i%2==0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# i =  1
# while i<= 10:
#     if(i%2!=0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# num = [1,2,3,4,5,6]
# for val in num:
#     print(val)

# num = [1,2,3,4,5,6]
# for val in num:
#     print(val)
# else:
#     print("end")

# str =  'SHANKAR GOUDA'
# for char in str:
#     if(char == "A"):
#         print("A found")
#         break
#     print(char)
# else:
#     print("end")

# i = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for n in i:
#     print(n)

# i = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# x = 9
# idx = 0
# for n in i:
#     if(n == x):
#         print("found",idx)
#     idx += 1

# for e in range(2,10,2):
#     print(e)

# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)
# for i in range(2,21,2):
#     print(i)

# i =  int(input("enter : "))
# for n in  range(1,11):
#     print(n*2)

# for i in range(8):
#     pass
# print("print")

# n = 6
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("total sum=",sum)

# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i +=1
# print("total=",sum)

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i +=1
# print("total=",fact)

n = 4
fact  = 1
for i in range(1, n+1):
    fact *= i
print("fact=",fact)

