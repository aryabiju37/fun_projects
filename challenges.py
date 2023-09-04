from threading import *
# 1 Reverse A string

# s = input("enter the string to be reversed: ")
# lststr = []
# for i in range(len(s)):
#     lststr.append(s[len(s)-i-1])
# print("".join(lststr))

# 2.Balanced brackets
# def is_blanced(lstbrackets):
#     cnt = 0 
#     for char in lstbrackets:
#         if(char == "["):
#             cnt += 1
#         if(char == "]"):
#             cnt -= 1
#     if cnt == 0:
#         return True
#     else:
#         return False

# isbalanced = is_blanced("[[1, True, [],[1],[2,3]]")
# print(isbalanced)

#3 Write a function called list_check, which accepts a list and 
# returns True if each value in the list is a list. Otherwise the function should return False.

'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''
# def list_check(lstlist):
#     lstchecks = []
#     for item in lstlist:
#         if type(item) is not list:
#             lstchecks.append(False)
#         else:
#             lstchecks.append(True)
#     if False in lstchecks:
#         return False
#     else:
#         return True
        
# check = list_check([[],[1],[2,3]])
# print(check)

# 4 remove every other value
'''
Write a function called remove_every_other that accepts a list 
and returns a new list with every second value removed.
'''
'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

# def remove_every_other(lstnumbers):
#     del lstnumbers[1:-1:2]
#     return lstnumbers

# lstnums = remove_every_other([5,1,2,4,1])
# print(lstnums)

'''
Write a function called sum_pairs which accepts a list and a number and 
returns the first pair of numbers that sum to the number passed to the function.
'''
'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

# def sum_pairs(lstnums,num):
#     sum = 0
#     lstreturn = []
#     for i in range(len(lstnums)):
#         if i != len(lstnums)-1:
#                 if lstnums[i]+lstnums[i+1] == num :
#                     return lstnums[i:i+2]
        
        
#         else:
#             return lstreturn

# lstrem = sum_pairs([11,20,4,2,1,5], 100)
# print(lstrem)

'''
vowel_count
Write a function called vowel_count that accepts a string and returns a dictionary 
with the keys as the vowels and values as the count of times that vowel appears in the string.
'''

'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''
# def vowel_count(strVowel):
#     a_count = 0
#     e_count = 0
#     i_count = 0
#     o_count = 0
#     u_count = 0
#     dictVowel = {}
#     for char in strVowel:
#         if char == "a" or char=="A":
#             a_count += 1
#             dictVowel.update({"a":a_count})
#         if char == "e" or char=="E":
#             e_count += 1
#             dictVowel.update({"e":e_count})
#         if char == "i" or char=="I":
#             i_count += 1
#             dictVowel.update({"i":i_count})
#         if char == "o" or char=="O":
#             o_count += 1
#             dictVowel.update({"o":o_count})
#         if char == "u" or char=="U":
#             u_count += 1
#             dictVowel.update({"u":u_count}) 
#     return dictVowel

# dictVow = vowel_count('Eleene')
# print(dictVow)

'''
Write a function called titleize which accepts a string of words and returns a 
new string with the 
first letter of every word in the string capitalized.
'''        

'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''
# def titleize(strText):
#     lstWords = strText.split()
#     lstSpliced = []
#     print(lstWords)
#     for wrd in lstWords:
#         wrd = wrd[:-1].upper()+wrd[-1].lower()
        
#         lstSpliced.append(wrd)
#     return " ".join(lstSpliced)
# strLst = titleize('oNLy cAPITALIZe fIRSt')
# print(strLst)
'''
Write a function called find_factors which accepts a number and returns a list of all 
of the numbers which are is divisible by starting from 1 and going up to the number.
'''

'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''
# l = Lock()
# def find_factors(num):
#     l.acquire()
#     factors = []
#     i = 1
#     while i <= num:
#         if (num % i) == 0:
#             factors.append(i)
#         i += 1
#     l.release()
#     return factors

# def display(num):
#     print(f"The factors of, {num} is {find_factors(num)}")

# t1 = Thread(target=display,args=(412345678,))
# t1.start()  



'''
includes
Write a function called includes which accepts a collection, a value, and an optional starting index. 
The function should return True if the value exists in the collection when we search starting from the starting index. 
Otherwise, it should return False.

The collection can be a string, a list, or a dictionary. If the collection is a string or array, the third parameter is a
starting index for where to search from. If the collection is a dictionary, the function searches for the value among values 
in the dictionary; since objects have no sort order, the third parameter is ignored.
'''  
'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''
'''
new challenge
'''
'''
Factorial of a number
'''
# l = RLock()
# result = 1
# def factorial(num):
#     l.acquire()
#     if num == 0:
#         result = 1
#     else:
#         result = num*factorial(num-1)
#     l.release()
#     return result

# def display(num,num1,num2):
#     print(f"the factorial of {num} is {factorial(num)} checking..{num1},{num2}")
# t1 = Thread(target = display,args=(5,6,7))
# t1.start()

# class Test:
#     a = 10
#     def __init__(self):
#         self.b = 20


# t = Test()
# print(t.__dict__)
# t.b = 777
# t.a = 888
# print(t.__dict__)


# arr = [10, 20, 30]
 
 
# def fun():
#     global arr
#     arr = [20, 30, 40]
 
 
# print("'arr' list before executing fun():", arr)
# fun()
# print("'arr' list after executing fun():", arr)

