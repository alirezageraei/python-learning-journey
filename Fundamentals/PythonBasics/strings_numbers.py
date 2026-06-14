###STR Combinations###
name = "Ali"
familyName = "Geraei"
Age = 23.3658

str = "Hello %s, we knew you as %s and we think you are %f YO" %(name, familyName, Age) #with %
print(str)

print('--------------------------------------------------------------')

str = "Hello {}, we knew you as {} and we think you are {} YO".format(name, familyName, int(Age)) #With format
print(str)
str = "Hello {0}, we knew you as {1} and we think you are {2} YO".format(name, familyName, Age) #with index format
print(str)
str = "Hello {nam}, we knew you as {famil} and we think you are {sen} YO".format(nam=name, famil=familyName, sen=int(Age)) #with name formatting format
print(str)

print('--------------------------------------------------------------')

str = f"Hello {name}, we knew you as {familyName} and we think you are {Age} YO"
print(str)

print('--------------------------------------------------------------')

###Number Exercise###


def Area(x):
    area = (x**2) * pi
    return area


r = int(input("Please Enter the radius value: "))
pi = 3.141592653592
pi = round(pi,2) #to make the calcaulation with 2 decimal places of PI
circleArea = Area(r)
print(f'{circleArea:.2f}') #to display up to 2 decimal places(Not in calculations)

print('--------------------------------------------------------------')

### Multiply chart ###

def MultiChart(mainNumber):
    n = mainNumber
    for i in range(1,11):
        r = n * i
        print(f"{n} * {i} = {r}")
        i += 1
    
N = int(input("Write your number:"))
MultiChart(N)

print('--------------------------------------------------------------')

### Name counter ###

def spaceCleaner(text):
    return text.replace(' ','')
    
            

firstName = input("enter your firstname:")
lastName = input("enter your lastname:")
fullName = firstName + ' ' + lastName
charCount = len(spaceCleaner(fullName))
upCase = fullName.upper()

print(f"first name:{firstName}")
print(f"last name:{lastName}")
print(f"full name:{fullName}")
print(f"full name in capital:{upCase}")
print(f"Characters count: {charCount}")
print(f"firstname first char is '{firstName[0]}' & lastname first char is '{lastName[0]}'")

print('--------------------------------------------------------------')

### playing with strings ###

# def count_words(text):
#     if not text or not isinstance(text, str):
#         return 0
#     return len(text.split())
# تابع بالا نیز راه مطمئن تری برای جداسازی کلمات است به شکلی که غیر رشته ها را دریافت نمیکند.

# def replaceChar(text,current_sign,replacement):
#     result=''
#     for i in range(0, len(text)):
#         if text[i] != current_sign:
#             result += text[i]
#         else: result += replacement
#     return result
# دست نویس شده تابع replace با استفاده از مهارت فردی
s = input("write your sentence:")
reversed_s = s[::-1]
wordCounter = len(s.split())
replace_spaces = s.replace(' ','-')
# replace_spaces= replaceChar(s,' ','-')  # تابع دست نویس

print(f"reversed: {reversed_s}")
print(f"words count: {wordCounter}")
print(f"dash added: {replace_spaces}")

print('--------------------------------------------------------------')

### Simple graphical grade chart ###

import statistics

lessons = ['math', 'physics', 'history']
grades= []
for i in range(len(lessons)):
    grade = float(input(f"Enter your {lessons[i]} grade:"))
    if 0 <= grade <= 20:
        grades.append(grade)

mean = statistics.mean(grades)
print(f"\nyour'e average score is: {mean}")
print('-'*20)

if mean <= 10:
    print("\nUnfortunately, you Failed!❌")
else: print("\nCongratulations, you have Passed!✅")
print('-'*20)

print("you're graphical performance:\n" + 30*'='+'\n')

for i in range(len(lessons)):
    stars = '*' * int(grades[i])
    print(f'{lessons[i]}:' + stars)
print('\n'+30*'-')

print('----------------------------------------------------------------')

### Temperature convertor ###

tempC = float(input("Enter the temperature in celisius:"))
# فارنهایت = (C × 9/5) + 32
# کلوین = C + 273.15
tempF = (tempC * 9.5) + 32
tempK = tempC + 273.15

print('='*30)

print(f"°C: {tempC:.2f}")
print(f"°F: {tempF:.2f}")
print(f"K: {tempK:.2f}")

print('='*30)

print('-----------------------------------------------------------------')

""" New Practices """
### max, min, avg ###
from random import randint as ri

l = [ri(-1000,1000) for i in range(50)]

max_value = 0
for i in l:
    ''' Finds maximum value '''
    if i >= max_value:
        max_value = i
print(max_value)

min_value = 0
for i in l:
    ''' Finds minimum value '''
    if i <= min_value:
        min_value = i
print(min_value)

sum_value = 0
for i in l:
    ''' makes sum of values '''
    sum_value += i
avg_value = sum_value / len(l) # makes avg from sum
print(avg_value)

### slicing, list item filtering ###

l = ['ali','reza','sara','hossein','samira','sasan','zahra','nazanin','saman','fatemeh']

first_three = [i for i in l[0:3]]
last_three = [i for i in l[-4:-1]]
even_index = [i for i in l if l.index(i)%2==0]
even_len = [i for i in l if len(i)%2==0]

print(first_three)
print(last_three)
print(even_index)
print(even_len)

### word counter dict ###

letture = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Egestas purus viverra accumsan in nisl nisi. Arcu cursus vitae congue mauris rhoncus aenean vel elit scelerisque. In egestas erat imperdiet sed euismod nisi porta lorem mollis. Morbi tristique senectus et netus. Mattis pellentesque id nibh tortor id aliquet lectus proin. Sapien faucibus et molestie ac feugiat sed lectus vestibulum. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Dictum varius duis at consectetur lorem. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Velit ut tortor pretium viverra suspendisse potenti nullam. Et molestie ac feugiat sed lectus. Non nisi est sit amet facilisis magna. Dignissim diam quis enim lobortis scelerisque fermentum. Odio ut enim blandit volutpat maecenas volutpat. Ornare lectus sit amet est placerat in egestas erat. Nisi vitae suscipit tellus mauris a diam maecenas sed. Placerat duis ultricies lacus sed turpis tincidunt id aliquet. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Egestas purus viverra accumsan in nisl nisi. Arcu cursus vitae congue mauris rhoncus aenean vel elit scelerisque. In egestas erat imperdiet sed euismod nisi porta lorem mollis. Morbi tristique senectus et netus. Mattis pellentesque id nibh tortor id aliquet lectus proin. Sapien faucibus et molestie ac feugiat sed lectus vestibulum. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Dictum varius duis at consectetur lorem. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Velit ut tortor pretium viverra suspendisse potenti nullam. Et molestie ac feugiat sed lectus. Non nisi est sit amet facilisis magna. Dignissim diam quis enim lobortis scelerisque fermentum. Odio ut enim blandit volutpat maecenas volutpat. Ornare lectus sit amet est placerat in egestas erat. Nisi vitae suscipit tellus mauris a diam maecenas sed. Placerat duis ultricies lacus sed turpis tincidunt id aliquet."

# lst_res = []
# word = ''
# for i in letture:
#     if i == ' ':
#         lst_res.append(word)
#         word = ''
#         continue
#     word += i
""" instead of spliting words with loops
we can use str.split() """
words = letture.split()

res = {}
for i in words:
    if i in res:
        ''' if the word exist more than 1 time,
         counter will count it '''
        res[i] += 1
    else:
        ''' if the word exist only 1 time,
         counter will be set on 1 '''
        res[i] = 1

print(res)

### remove repeated values ###

l = [1,2,33,3,4,3,3,5,6,85,57,95,64,85,6,3,12,5,8,6,3,5,33,25,95,6,12,8,0]

# res = []
# for i in l:
#     counter = 0
#     for j in l:
#         if i == j:
#             counter += 1
#     if counter == 1:
#         res.append(i)
''' This is not Optimized
    we can do this instead:
'''
import collections as col
""" we have a new package and
    a more advanced list comperehention
"""
counter = col.Counter(l)
res = [i for i, count in counter.items() if count == 1]
print(res)

### dict value avg ###

grades = {
    'ali': [20,19,16],
    'sama': [17,18,19],
    'saba': [12,14,15]
}

for k, v in grades.items():
    print(f"{k} has the avg grade: {sum(v) / len(v):.2f}")

### print bigger than 10 even numbers ###
    
l = [1,10,24,85,77,158,957,6,4,65,56,46,542,33,3,4,3,3,5,6,85,57,95,64,85,6,3,12,5,8,6,3,5,33,25,95,6,12,8,0]

res = [i for i in l if i%2==0 and i > 10]
print(res)

### Nested dictionary ###
books = []

for i in range(3):
    title = input(f"Title: ")
    author = input(f"Author: ")
    year_str = input(f"Pubsish year: ")
    year = int(year_str) # تبدیل سال به عدد صحیح
    books.append({"Title": title, "Author": author, "year": year})

res = {}
for item in books:
    """ adding to dicts nested dict """
    res[f"book {books.index(item) + 1}"] = item

# newest = ''
# sel_year = year
# for k in res.keys():
#     if res[k]['year'] > sel_year:
#         newest = k
# print(f"the last published book is: {newest}")
""" instead of these we can
    write our code thisway:
"""
newest_book = max(books, key=lambda x: x['year'])

for k,v in newest_book.items():
    print(k, ':', v)

### word counter and cleaner ###
""" this section just as two section earllier
    has an useful Subject as collections
"""
from collections import Counter
s = input('Enter you sentence: ')

cleaned_s = s.replace(',','',).replace('.','').replace('?','',).replace('!','')

words = cleaned_s.split()

counter = Counter(words)
single_words = [item for item , count in counter.items() if count == 1]

# highest_count = 1
# most_repeated = ''
# for k, v in counter.items():
#     if v > repeat:
#         highest_count = v
#         most_repeated = k 
""" this code works But we can do it far more
    simple with collections.most_common()
"""
most_common_item = counter.most_common(1)
if most_common_item:
    most_repeated, repeat_count = most_common_item[0]
print(f"only 1 repeated words: {single_words}")
print(f"most repeated word is: {most_repeated}")
print(f"words count is: {len(words)}")

### Numeric domain check ###
""" It's better to not use print() directly in place """
n = int(input("Enter the number: "))

if 10 <= n <= 50:
    message = f"{n} is in domain"
else:
    message = f"{n} is NOT in domain"

""" we can also do this: """
message = f"{n} is in domain" if 10 <= n <= 50 else f"{n} is NOT in domain"
print(message)

### double (=) check ###

l1 = [1,2,5,4,8,6,5,2,4,8,2,3,4,8,9,7,5,1]
l2 = [6,4,5,8,4,2,1,4,7,3,6,5,2,1,5,2,1,7]

operator = f"Positive" if sum(l1) == sum(l2) else "Negative"
print(operator)

### Name comparing by Unicode ###

def compare_names():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    # String comparison in Python is lexicographical.
    # It compares characters from left to right using Unicode values.

    if name1 == name2:
        print("Both names are the same.")
    elif name1 > name2:
        print(f"'{name1}' is lexicographically greater than '{name2}'.")
    else:
        print(f"'{name2}' is lexicographically greater than '{name1}'.")


compare_names()

### Login access check ###

def access(user, passw):
    # is_admin = False
    # user_tuple = tuple([user, passw]) 
    # admin_list = [("admin", "1234"), ("alireza", "1221")]
    # if user_tuple in admin_list:
    #     is_admin = True 
    # return "access granted" if is_admin else "access denied"
    """
    We can do this instead
    this method called 'Early Return'
    """
    admin_list = [("admin", "1234"), ("alireza", "1221")]
    if (user, passw) in admin_list:
        return "access granted"
    return "access denied"
    
username = input("Type your username: ")
password = input("Type your Password: ")

print(access(username, password))

### Is_Triangle? ###

# def is_triangle(a,b,c):
#     max_edge = max(a,b,c)
#     a,b,c = a / max_edge, b / max_edge, c / max_edge
    
#     if (a + b + c) > 2.0:
#         return "these numbers can be the edges of a Triangle"
#     else:
#         return "these numbers can NOT be the edges of a Triangle"
    
# print(is_triangle(5,5,10)) 
""" 
    to prevent zero division or same errors
    we can write this code thisway:
"""
def is_triangle(a, b, c):
    # بررسی اینکه آیا تمام اضلاع مثبت هستند
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input: All edges must be positive."
        
    # لیست اضلاع
    edges = sorted([a, b, c])
    
    # در یک مثلث، مجموع دو ضلع کوچک‌تر باید بزرگتر از ضلع بزرگتر باشد
    if edges[0] + edges[1] > edges[2]:
        return "These numbers can form a triangle."
    else:
        return "These numbers can NOT form a triangle."

print(is_triangle(5, 5, 10)) # خروجی: ...NOT form a triangle
print(is_triangle(3, 4, 5))  # خروجی: These numbers can form a triangle

### symmetric difference ###
""" This is a great example """
mid_term_grades = {
    'dini':19,
    'riazi':19,
    'arabi':19,
    'farsi':19,
}
end_term_grades = {
    'honar':19,
    'arabi':19,
    'farsi':19,
    'dini':19,
}
# کلیدهایی که فقط در یکی از دیکشنری‌ها هستند
only_one = set(mid_term_grades.keys()) ^ set(end_term_grades.keys())

for k in only_one:
    if k in mid_term_grades:
        print(f"{k} is not exist in end-term")
    else:
        print(f"{k} is not exist in mid-term")

### Unordered compare of lists ###
        
"""
l1 = [1,2,3,6,4,5]
l2 = [4,2,3,1,5,6]

only_in_one = set(l1) ^ set(l2)

if len(only_in_one) == 0:
    print("these list are the same 'Unordered'")
else:
    print("these list are different")
"""
"""
    there is a problem, sets are not
    recognize repeated args, so if one 
    of the list has a repeated arg,it
    will show they are same, to fix
    it we can do it thisway:
"""
l1 = [1, 2, 2, 3, 6, 4, 5]
l2 = [4, 2, 3, 1, 5, 6, 2]

# روش 1: استفاده از Counter (بهترین راه)
from collections import Counter
if Counter(l1) == Counter(l2):
    print("these lists are the same 'Unordered'")
else:
    print("these lists are different")

# روش 2: بدون کتابخانه (با حذف عناصر)
def are_same_unordered(list1, list2):
    temp = list2[:]  # کپی
    for item in list1:
        if item in temp:
            temp.remove(item)
        else:
            return False
    return len(temp) == 0

if are_same_unordered(l1, l2):
    print("these lists are the same 'Unordered'")
else:
    print("these lists are different")

### XOR ###
    

a = False
b = True
"""
if a != b:
    res = True
    print(res)
"""
"""
    We can do this better like these:
"""
print(a != b)  
print("-------------------------------------")
print(a ^ b) 
print("-------------------------------------")
def xor(x, y):
    return x != y

print(xor(a, b))  
print("-------------------------------------")

print((a or b) and not (a and b))  

### multiple condition on list ###

MMd = {
    'Age': 23,
    "has_lisence": True
}
Sama = {
    'Age': 22,
    "has_lisence": False
}
Saba = {
    'Age': 17,
    "has_lisence": False
}

lst = list([MMd,Sama,Saba])
lst_2 = [i for i in lst if i['Age'] > 18 and i["has_lisence"]]
print(lst_2)