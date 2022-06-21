######################## string #########################
######################## task 1  #######################

# st = 'ApplE'

# upper = 0
# lower = 0
# st1 = ""

# for i in range(len(st)):
#     if st[i].isupper():
#         upper = upper + 1
#     elif st[i].islower():
#         lower = lower + 1

# if upper > lower:
#     st = st.upper()
# elif upper <= lower:
#     st = st.lower()

# print(st)


############################  task 2  ###############################

# st = 'ADDD'

# num = 0
# char = 0

# for i in range(len(st)):
#     if st[i] >= "0" and st[i] <= "9":
#         num = num + 1
#     elif st[i]>= "a" and st[i] <= "z" or st[i] >= "A" and st[i] <= "Z":
#         char = char + 1

# if num == 0 and char > 0:
#     print("WORD")
# elif num > 0 and char == 0:
#     print("NUMBER")
# elif num > 0 and char > 0:
#     print("MIXED")
##########################  task 3  #############################

# st = "coDIng"

# fst = 0
# lst = 0

# for i in range(len(st)):
#     if st[i].isupper() and fst == 0:
#         fst = i
#     elif st[i].isupper() and fst != 0:
#         lst = i 

# if (lst - fst) > 1:
#     print(st[fst+1:lst])
# else:
#     print("BLANK")



#####################  Task 4  ###################################
# st1 = "dean"
# st2 = "tom"

# fst = ""
# lst = ""

# for i in range(len(st1)):
#     if st1[i] in st2:
#         fst = fst + st1[i]

# for i in range(len(st2)):
#     if st2[i] in st1:
#         lst = lst + st2[i]

# if len(fst) != 0 and len(lst) != 0:
#     print(fst + lst)
# else:
#     print("Nothing in common")


######################  Task 5  ###################################
# import re

# pss = "ohmybracu"

# def lower():
#     print("Lowercase missing")
# def upper():
#     print("Uppercase missing")
# def dgt():
#     print("Digit missing")
# def spcl():
#     print("Special missing")

# low = 0
# up = 0
# dg = 0
# spc = 0

# for i in range(len(pss)):
#     if pss[i].isnumeric():
#         dg += 1
#     elif pss[i].islower():
#         low += 1
#     elif pss[i].isupper():
#         up += 1
#     elif(bool(re.search('^[a-zA-Z0-9]*$', pss)) == False):
#         spc += 1

# if low != 0 and up != 0 and dg != 0 and spc != 0:
#     print("OK")
# if low == 0:
#     lower()
# if up == 0:
#     upper()
# if dg == 0:
#     dgt()
# if spc == 0:
#     spcl()




############################    LIST   ################################
########################################################################
#############################  Task 1 #################################

# ls = []
# ls1 = []
# cnt = []

# while True:
#     user = input()
#     if user != "STOP":
#         ls.append(user)
#     else:
#         break

# for i in range(len(ls)):
#     if ls[i] not in ls1:
#         x = ls.count(ls[i])
#         ls1.append(ls[i])
#         cnt.append(x)

# for i in range(len(ls1)):
#     print(f"{ls1[i]} - {cnt[i]} times")


#############################  Task 2  #############################

# n = int(input("input de beta: "))
# f_ls = []
# flag = 0

# for i in range(n):
#     ls = [int(i) for i in input().split(" ")]
#     cnt = 0
#     for j in range(len(ls)):
#         cnt = cnt + ls[j]
#     if flag < cnt:
#         flag = cnt
#         f_ls = ls.copy()

# print(flag)
# print(f_ls)

    
########################  Task 3  #####################################

# while True:
#     flag = 0
#     temp = 0
#     ls = []
#     # user = input()
#     # ls.append(user)
#     ls = [i for i in input("please enter input: ").split(" ")]
#     temp = len(ls)
#     if "STOP" in ls:
#         break
#     for i in range(temp-1):
#         if abs(int(ls[i]) - int(ls[i+1])) > temp:
#             flag += 1
    
#     if flag == 0:
#         print("UB Jumper")
#     else:
#         print("Not UB Jumper")


#############################  Task 4  ###################################

# n, k = input("please enter input: ").split()

# flag = 0
# ls = []
# for i in range(int(n)):
#     user = int(input("data: "))
#     if (user + int(k)) <= 5:
#         flag += 1

# print(flag//3)


######################################################################
#####################  Dictionary  ####################################
#######################  Task 1     ###########################################

# d1 = {"a": 100, "b": 100, "c": 200, "d": 300}
# d2 = {"a": 300, "b": 200, "d": 400, "e": 200}
# final = {}
# ls = []

# for i in d1.keys():
#     for j in d2.keys():
#         if i == j:
#             res = d1.get(i) + d2.get(j)
#             d1[i] = res
# d2.update(d1)
# for i in sorted(d2):
#     final[i] = d2[i]

# print(final)

# for i in final.values():
#     if i not in ls:
#         ls.append(i)
# ls.sort()
# print(tuple(ls))


########################  Task 2  ##################################

# dict = {}


# while True:
#     user = input("enter data: ")
#     if user == "STOP":
#         break
#     else:
#         if user not in dict.keys():
#             dict[user] = 1
#         elif user in dict.keys():
#             dict[user] = dict.get(user) + 1

# for key, value in dict.items():
#     print(f"{key} - {value} times")

######################## Task 3  ###################################

# dict = {"key1" : "value1", "key2" : "value2", "key3" : "value1"}
# dict1 = {}
# for x in dict.items():
#     if x[1] not in dict1.keys():
#         dict1[x[1]] = []

#     dict1[x[1]].append(x[0])

# print (dict1)


#######################  Task 4  ####################################

# dict = {"1": [".", ",", "?", "!", ":"], "2" : ["A", "B", "C"], "3" : ["D", "E", "F"], "4" : ["G", "H", "I"], 
# "5" : ["J", "K", "L"], "6" : ["M", "N", "O"], "7" : ["P", "Q", "R", "S"], "8" : ["T", "U", "V"], "9" : ["W", "X", "Y", "Z"], "0" : [" "]}

# user = input("please enter input: ")
# user = user.upper()
# rs = ""

# for i in range(len(user)):
#     #temp = ""
#     for j in range(0, 10):
#         temp = dict.get(str(j))
#         if user[i] in temp:
#             rs = rs + ((temp.index(user[i])+1)*str(j))
#             break

# print(rs)


#######################  Function   #################################
#####################################################################
########################  Task 1  ##################################

# def bmi(cm, kg):
#     m = (cm/100)
#     rs = kg/(m*m)
#     print("Score is", round(rs, 1), end="")
#     if rs < 18.5:
#         print(". You are Underweight")
#     elif rs >= 18.5 and rs <= 24.9:
#         print(". You are Normal")
#     elif rs >= 25 and rs <= 30:
#         print(". You are Overweight")
#     elif rs > 30 :
#         print(". You are Obese")

# cm  = float(input("enter height: "))
# kg = float(input("enter your weight: "))

# bmi(cm, kg)

#######################  Task 2  #########################################

# def op():
#     user = [int(i) for i in input().split(",")]
#     rs = 0
#     dv = user[2]
#     for i in range(user[0], user[1]):
#         if i % dv == 0:
#             rs = rs + i
#     print(rs)

# op()


#########################  tASK 3   #################################

# def op(fd, area = "Mohakhali"):
#     if fd == "BBQ Chicken Cheese Burger":
#         cost = 250
#     elif fd == "Beef Burger":
#         cost = 170
#     elif fd == "Naga Drums":
#         cost = 200
#     tax = cost * (8/100)
#     if area == "Mohakhali":
#         cost = cost + 40 + tax
#     else:
#         cost = cost + 60 + tax
#     return cost

# fd = input("food:")
# area = input("area: ")

# print(op(fd, area))

######################### Task 4  ############################

# def replace_domain(check, new, old = " "):
#     flag = 0
#     index = 0
#     if old in check:
#         flag = 1
#         for i in range(len(check)):
#             if check[i] == "@":
#                 index = i
#                 break
#     if flag != 0:
#         print("Changed: ",check[0:index+1] + old)
#     else:
#         print("Unchanged:", check)
        


# replace_domain("alice@sheba.com", "sheba.xyz")


######################  Task 5  #####################################

# def fn():
#     st = "hello"

#     ls = ""
#     ls2 = ""

#     for i in range(len(st)):
#         if st[i] != " ":
#             ls = ls + st[i]

#     for i in range(-1, -len(ls)-1, -1):
#         ls2 = ls2 + ls[i]

#     if ls == ls2:
#         print("Palindrome")
#     else:
#         print("Not palindrome")

# fn()


############################   Task 6   #############################

# def cap():
#     st = "my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily.do you know my pet dog's name? i love my pet very much."
#     res = st[0].upper()

#     n = 0

#     for i in range(1, len(st)):
#         if (st[i] != "." or st[i] != "!" or st[i] != "?") and n == 1 and st[i] != "i":
#             if st[i] != " ":
#                 n = 0
#                 res = res + st[i].upper()
#             else:
#                 res = res + st[i]
#         elif (st[i] == "." or st[i] == "!" or st[i] == "?") and n == 0 and st[i] != "i":
#             n = 1
#             res = res + st[i]
#         elif (st[i] != "." or st[i] != "!" or st[i] != "?") and n == 0 and st[i] != "i":
#             res = res + st[i]
#         elif st[i] == "i":
#             if st[i-1] == " " and (st[i+1] == " " or st[i+1] == "." or st[i+1] == "!" or st[i+1] == "?"):
#                 res = res + st[i].upper()
#             else:
#                 res = res + st[i]
#     print(res)


# cap()








