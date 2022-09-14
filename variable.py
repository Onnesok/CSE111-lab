# Escape sequence [most common method]

s = "yo yo \"python\""
print(s)

s1 = "hello \n there"
print(s1)

s2 = "hey \t there"
print(s2)

s3 = "omg \b there"
print(s3)

#string formatting

n1 = "hello {}, I am {}".format("ratul", "onnesok")
print(n1)

n2 = "hello {1}, I am {0}".format("ratul", "onnesok")
print(n2)

n3 = "hello {yo}, I am {yo1}".format(yo = "ratul", yo1 = "onnesok")
print(n3)

# Number formatting
n4 = "yo {}, can you lend me {:d} taka".format("ratul", 100)  # here d represents integer number....... recal C programming language scan method
print(n4)

n5 = "yo {}, can you lend me {:f} taka".format("ratul", 10.5550)  # here f represents floating number
print(n5)


n5 = "yo {}, can you lend me {:5.2f} taka".format("ratul", 10.5550)  # here .2 means it will print 2 digits after decimal and 5 means total number including .
print(n5)


###############################################################

# string creation

# print("CSE111")
# print("CSE')
# print('CSE111")
# print("CSE!@^78/*-./, ][{}\|`~")








# String creation with multiple lines

# courses = '''CSE111
# CSE110
# CSE220'''
# print(courses)

# testing with single quote

# courses_1 = "CSE111
# CSE110
# CSE220"
# print(courses_1)

# What about the space inside the string?

# courses_2 = "CSE111\n CSE110\n CSE220"
# print(courses_2)

# are "r" and "R" same??







# var = "\\" + "n"
# print(var)







# indexing of string

# test = "computer science"
# print(test[0]) #positive indexing
# print(test[-1]) #negative indexing
# print(test[8]) #space?

#indexing of a string
#C  S  E
#0  1  2 (positive indexing)
#-3 -2 -1 (negative indexing)

# What about the error for wrong index?
# print(test[20])

#Can we use other data types other than int while indexing?
# print(test[8.0])








# using len function to know the length of a string

# print(len("Coding"))
# s = "coding"
# print(s[len(s)-1])










# Mutability of a string

# s = "CSE111"
# s[5] = "0"
# print(s)

# s = "CSE110"
# print(s)










# iterating a string

# s = "programming"

# index = 1
# while index < len(s):
#   print(s[index])
#   index += 2

# for index in range(len(s)):
#   print(s[index])

# for char in s:
#   print(char)

# for index in range(0,len(s),2): #iterating even indexes
#   print(index)
#   print(s[index])

# for index in range(1,len(s),2): #iterating odd indexes
#   print(index)
#   print(s[index])










# ======> string operations <===========

#concating strings

# print("CSE" + "11" + "0")

# str1 = "Python"
# print(str1 + " programming")










#delete string

# test = "cricket"
# del test[0]
# del test
# print(test)









#string repetition

# print("a" * 3)

#we can use a for/while loop too










#slicing a string

# string = "cricket"

# print(string[:])
# print(string[2:])
# print(string[:3])
# print(string[2:-2])
# print(string[-4:-1])
# print(string[-1:-1])
# print(string[5:2])

# now try with step

# print(string[2:3:2])
# print(string[-1:-len(string)-1:-1]) #reverse a string
# print(string[::-1]) #reverse a string
# print(string[-1::-1]) #reverse a string








#membership test

# sample = "we are playing"

# print("are" in sample)

# if "play" in sample:
#   print(True)









# Escape sequence

# str = "Python 'is' easy"
# print(str)

# str = 'Python "is" easy'
# print(str)

# str = 'Python \'is\' easy'
# print(str)

# str = "Python \"is\" \"so\" easy"
# print(str)








# #formating

# # default(implicit) order
# str = "Hello {}, Welcome to {}.".format("User", "python")
# print(str)

# # order using positional argument
# str = "Hello {0}, Welcome to {1}.".format("User", "python")
# print(str)

# # order using positional argument
# str = "Welcome to {1}, hello{0}.".format("User", "python")
# print(str)

# # order using keyword argument
# str = "Hello {user}, welcome to{lang}.".format(user="User", lang="python")
# print(str)









#number formating

# str = "Hello {0}, can you lend me {1:d}$?".format("Bob", 100)
# print(str)

# str = "I am {0}, {1}. I have only {2:.2f}$.".format("sorry", "Alice", 50.95876)
# print(str)







#ASCII
# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))

# print(chr(65))
# print(chr(90))
# print(chr(97))
# print(chr(122))







#string functions

# str = "HeLLo FrIeNDs"
# print(str.lower())

# str = "HeLLo FrIeNDs"
# print(str.upper())

# str = " HeLLo FrIeNDs "
# print(str.strip())

# str = "XYThis is an example sentence.XY"
# print(str.strip("X"))

# str = " XYThis is an example sentence.XY "
# print(str.strip(" X"))

# str = "This is an example sentence."
# print(str.count("is"))
# print(str.count("is", 4))
# print(str.count("is", 2, 8))

# str = "This is an example sentence."
# print(str.startswith("This"))
# print(str.startswith("This", 5, 8))

#practice endswith
# str = "This is an example sentence."
# print(str.replace("is", "_"))
# print(str.replace("is", "_", 1))
