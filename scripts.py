#### Introduction (7) ####

# (1) Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# (2) Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif (n % 2 == 0) and 2 < n < 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 < n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

# (3) Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# (4) Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# (5) Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i**2)

# (6) Write a function
def is_leap(year):
    leap = False
    # leap is a boolean variable initially set False.
    # The code modifies "leap" first checking if year can be
    # evenly divided by 4; if not the function returns leap (= False).
    # Otherwise the function checks if year can be evenly divided by 100;
    # if this condition is satisfied, finally verifies if year can be
    # evenly divided by 400.
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

# (7) Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")


#### Basic Data Types (6) ####

# (8) List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    app = [[a, b, c] for a in [ a for a in range(x+1) ] for b in [ b for b in range(y+1) ] for c in [ c for c in range(z+1) ]]
    result = []
    for i in app:
        summ = 0
        for j in i:
            summ += j
        if summ != n:
            result.append(i)
    print(result)

# (9) Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    massimo = max(arr_list)
    while massimo in arr_list:
        arr_list.remove(massimo)
    print(max(arr_list))

# (10) Nested Lists
if __name__ == '__main__':
    records = []
    score_list = []
    score_name = []
    for _ in range(int(input())):
        nest_lista = []
        name = input()
        score = float(input())
        score_list.append(score)
        score_name.append(name)
        nest_lista.append(name)
        nest_lista.append(score)
        records.append(nest_lista)

minimum = min(score_list)
app = score_list
app_2 = app
while minimum in app:
    app_2.remove(minimum)

s_lowest_grade = min(app_2)
second_score_name = []

for i in range(0, len(records)):
    if records[i][1] == s_lowest_grade:
        second_score_name.append(records[i][0])

second_score_name = sorted(second_score_name)

for i in second_score_name:
    print(i)

# (11) Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    selected_value = student_marks[query_name]
    app = 0
    for i in selected_value:
        app += i
    mean = app / len(selected_value)
    formatted_number = "{:.2f}".format(mean)
    print(formatted_number)

# (12) Lists
if __name__ == '__main__':
    N = int(input())
    res = []
    b = []
    for i in range(N):
        b.append(input())

    split_list = []

    for item in b:
        split_items = item.split()
        split_list.extend(split_items)

    for i in range(len(split_list)):
        if split_list[i] == "insert":
            res.insert(int(split_list[i + 1]), int(split_list[i + 2]))
        if split_list[i] == "print":
            print(res)
        if split_list[i] == "remove":
            res.remove(int(split_list[i + 1]))
        if split_list[i] == "append":
            res.append(int(split_list[i + 1]))
        if split_list[i] == "sort":
            res = sorted(res)
        if split_list[i] == "pop":
            res.pop()
        if split_list[i] == "reverse":
            res.reverse()

# (13) Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

#### Strings (14) ####

# (14) sWAP cASE
def swap_case(s):
    string = ""
    for i in s:
        if i.isupper() == True:
            string += i.lower()
        else:
            string += i.upper()
    return(string)

# (15) String Split and Join
def split_and_join(line):
    # write your code here
    a = line.split(" ")
    app = "-".join(a)
    return(app)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# (16) What's Your Name?
def print_full_name(first, last):
    # Write your code here
    return(print(f"Hello {first} {last}! You just delved into python."))

# (17) Mutations
def mutate_string(string, position, character):
    l = list(string)
    l[position] = str(character)
    string = ''.join(l)
    return(string)

# (18) Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i: i + len(sub_string)] == sub_string:
            count += 1
    return (count)

# (19) String Validators
if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in s:
        if i.isalnum() == True:
            alnum = True
        if i.isalpha() == True:
            alpha = True
        if i.isdigit() == True:
            digit = True
        if i.islower() == True:
            lower = True
        if i.isupper() == True:
            upper = True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

# (20) Text Alignment
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# (21) Text Wrap
import textwrap

def wrap(string, max_width):
    stra = textwrap.fill(string, max_width)
    return(stra)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# (22) Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
input_utente = input()

valori = input_utente.split()
N = int(valori[0])
M = int(valori[1])

for i in range(0, N//2):
    print( "-" * int( (((M - 3) / 2) - 3*i) ) , end="" )
    print(".|", end="")
    print("..|" * 2 * i, end="")
    print(".", end="")
    print( "-" * int( (((M - 3) / 2) - 3*i) ) )

print( int((M-7) / 2) * "-", end="")
print("WELCOME", end="")
print( int((M-7) / 2) * "-")

for i in range(N//2 - 1, -1, -1):
    print( "-" * int( (((M - 3) / 2) - 3*i) ) , end="" )
    print(".|", end="")
    print("..|" * 2 * i, end="")
    print(".", end="")
    print( "-" * int( (((M - 3) / 2) - 3*i) ) )

# (23) String Formatting
def print_formatted(number):
    # your code goes here
    l=len(bin(number)[2:])
    for i in range(1,number+1):
        oct_num = str(oct(i))
        hex_num = str(hex(i)).upper()
        bin_num = str(bin(i))
        print(str(i).rjust(l,' '),oct_num[2:].rjust(l,' '),hex_num[2:].upper().rjust(l,' '),bin_num[2:].rjust(l,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# (24) Alphabet Rangoli
letters = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    # your code goes here
    # First Line
    print((size - 1) * 2 * "-", end="")
    print(letters[size - 1], end="")
    print((size - 1) * 2 * "-", end="")
    print()

    # From second to (size-1)th row
    for j in range(2, size):  # intera riga
        print((size - j) * 2 * "-", end="")  # first "-""
        print(f"{letters[size - 1]}-", end="")  # first letter
        for i in range(0, j - 2):  # center-left letters
            print(f"{letters[size - i - 2]}-", end="")
        print(f"{letters[size - j]}-", end="")  # center letter
        for k in range(j - 2, 0, -1):  # center-right letterss
            print(f"{letters[size - 1 - k]}-", end="")
        print(letters[size - 1], end="")  # last letter
        print((size - j) * 2 * "-", end="")
        print()

    # from (size)th row to the penultimate
    for j in range(size, 1, -1):  # intera riga
        print((size - j) * 2 * "-", end="")  # first "-""
        print(f"{letters[size - 1]}-", end="")  # first letter
        for i in range(0, j - 2):  # center-left letters
            print(f"{letters[size - i - 2]}-", end="")
        print(f"{letters[size - j]}-", end="")  # center letter
        for k in range(j - 2, 0, -1):  # center-right letterss
            print(f"{letters[size - 1 - k]}-", end="")
        print(letters[size - 1], end="")  # last letter
        print((size - j) * 2 * "-", end="")
        print()

    # Last row
    if size == 1:
        return ()
    print((size - 1) * 2 * "-", end="")
    print(letters[size - 1], end="")
    print((size - 1) * 2 * "-", end="")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# (25) Capitalize!
# Complete the solve function below.
def solve(s):
    s = s[0].upper() + s[1:]
    for i in range(0, len(s)):
        if s[i] == " ":
            s = s[0:i+1] + s[i+1].upper() + s[i+2:]
    return(s)

# (26) The Minion Game
vowels = "AEIOU"
def minion_game(string):
    # your code goes here
    points_stuart = 0
    points_kevin = 0
    for i in range(len(string)):
        if string[i] not in vowels:
            points_stuart += len(string) - i
        else:
            points_kevin += len(string) - i
    if points_stuart > points_kevin:
        return (print("Stuart", points_stuart))
    elif points_kevin > points_stuart:
        return (print("Kevin", points_kevin))
    else:
        return (print("Draw"))


if __name__ == '__main__':
    s = input()
    minion_game(s)

# (27) Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        res = ""
        for j in substring:
            if j not in res:
                res += str(j)
        print(res)
    return ()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#### Sets (13) ####

# (28) Introduction to Sets
def average(array):
    # your code goes here
    var = set(array)
    avg = sum(var) / len(var)
    return(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# (29) No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOU
n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
dictionary = {}
happiness = 0

for i in array:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

for i in A:
    if i in dictionary:
        happiness += dictionary[i]

for i in B:
    if i in dictionary:
        happiness -= dictionary[i]

print(happiness)

# (30) Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = set()

arr = list(map(int, input().split()))
for i in arr:
    a.add(i)
N = int(input())

b = set()
arr_2 = list(map(int, input().split()))
for j in arr_2:
    b.add(j)

c = a.difference(b)
d = b.difference(a)
res = c.union(d)
res = sorted(res)
for i in res:
    print(i)

# (31) Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))

# (32) Set .discard(), .remove() & .pop()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = map(int, input().split())
a = set(arr)

N = int(input())
b = []
for i in range(N):
    b.append(input())

split_list = []
for item in b:
    split_items = item.split()
    split_list.extend(split_items)

for i in range(len(split_list)):
    if split_list[i] == "pop":
        a.pop()
    if split_list[i] == "remove":
        a.remove(int(split_list[i + 1]))
    if split_list[i] == "discard":
        a.discard(int(split_list[i + 1]))

sum = 0
for i in a:
    sum += i

print(sum)

# (33) Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst_eng = list(map(int, input().split()))
set_eng = set(lst_eng)
b = int(input())
lst_fr = list(map(int, input().split()))
set_fr = set(lst_fr)

print(len(set_fr.union(set_eng)))

# (34) Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst_eng = list(map(int, input().split()))
set_eng = set(lst_eng)
b = int(input())
lst_fr = list(map(int, input().split()))
set_fr = set(lst_fr)

print(len(set_fr.intersection(set_eng)))

# (35) Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst_eng = list(map(int, input().split()))
set_eng = set(lst_eng)
b = int(input())
lst_fr = list(map(int, input().split()))
set_fr = set(lst_fr)

print(len(set_eng.difference(set_fr)))

# (36) Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst_eng = list(map(int, input().split()))
set_eng = set(lst_eng)
b = int(input())
lst_fr = list(map(int, input().split()))
set_fr = set(lst_fr)

print(len(set_fr.symmetric_difference(set_eng)))

# (37) Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = map(int, input().split())
A = set(arr)

N = int(input())

b = []
for i in range(2*N):
    b.append(input())

for i in range(0, len(b), 2):
    sets_prove = map(int, b[i + 1].split())
    sets = set(sets_prove)
    operation = b[i].split()[0]
    if operation == "intersection_update":
        A.intersection_update(sets)
    elif operation == "update":
        A.update(sets)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(sets)
    elif operation == "difference_update":
        A.difference_update(sets)

print(sum(A))

# (38) The Captain's Room
K = int(input())
room_numbers = input().split()
room_dict = {}

for room in room_numbers:
    if room in room_dict:
        room_dict[room] += 1
    else:
        room_dict[room] = 1
for room, count in room_dict.items():
    if count != K:
        print(room)

# (39) Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    a = int(input())
    arr = map(int, input().split())
    A = set(arr)

    b = int(input())
    arr_2 = map(int, input().split())
    B = set(arr_2)

    if A.intersection(B) == A:
        print(True)
    else:
        print(False)

# (40) Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
arr = map(int, input().split())
A = set(arr)

N = int(input())
var = True
for i in range(N):
    arr_2 = map(int, input().split())
    B = set(arr_2)
    if not (B.intersection(A) == B or len(A.difference(B)) < 1):
        var = False
print(var)

##### Collections (8) ####
# (41) collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
shoe_size = list(input().split())
dictionary = Counter(shoe_size)

N = int(input())
total_earnings = 0

for i in range(N):
    app = list(map(int, input().split()))
    size = str(app[0])
    prize = app[1]
    if size in dictionary and dictionary[size] > 0:
        dictionary[size] -= 1
        total_earnings += prize

print(total_earnings)

# (42) DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
def multiple_index(lista, a):
    indexes = []
    for index, element in enumerate(lista):
        if element == a:
            indexes.append(index)
    return(indexes)

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(0, n):
    d["A"].append(input())

for j in range(0, m):
    d["B"].append(input())

for i in d["B"]:
    if i in d["A"]:
        result = multiple_index(d["A"], i)
        for i in result:
            print(i + 1, end=" ")
        print()
    else:
        print(-1, end=" ")
        print()

# (43) Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())
columns = input().split()
total = 0

for i in range(N):
    students = namedtuple('Student', columns)
    column1, column2, column3, column4 = input().split()
    student = students(column1, column2, column3, column4)
    total += int(student.MARKS)

print('{:.2f}'.format(total / N))

# (44) collections.OrderedDict
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
ordered_dictionary = OrderedDict()

for i in range(N):
    lista = list(input().split())
    length = len(lista)
    item_name = ""
    for i in range(0, len(lista)-1):
        if i < (len(lista)-2):
            item_name += str(lista[i]) + " "
        else:
            item_name += str(lista[i])
    net_price = int(lista[-1])
    if item_name in ordered_dictionary:
        ordered_dictionary[item_name] = ordered_dictionary[item_name] + int(net_price)
    else:
        ordered_dictionary[item_name] = int(net_price)

for item_name, net_price in ordered_dictionary.items():
    print(item_name, net_price)

# (45) Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
elements = []
for i in range(n):
    elements.append(input())

dictionary = Counter(elements)
print(len(dictionary))
for i in dictionary:
    print(dictionary[i], end=" ")

# (46) Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
N = int(input())

for i in range(N):
    inputt = list(input().split())
    if len(inputt) == 1:
        move = inputt[0]
    else:
        move, number = inputt[0], inputt[1]
    if move == "append":
        d.append(int(number))
    if move == "appendleft":
        d.appendleft(int(number))
    if move == "pop":
        d.pop()
    if move == "remove":
        d.remove(int(number))
    if move == "extend":
        d.extend(int(number))
    if move == "popleft":
        d.popleft()

for i in d:
    print(i, end = " ")

# (47) Company Logo
# !/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    lista = []
    for i in range(len(s)):
        lista.append(s[i])
    dictionary = Counter(lista)
    dictionary_ordered = dict(sorted(dictionary.items(), key=lambda item: (-item[1], item[0])))

    counter = 0
    for key, value in dictionary_ordered.items():
        print(key, value)
        counter += 1
        if counter == 3:
            break

# (48) Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
def piling_cubes(cubes):
    l = len(cubes)
    last = max(cubes)
    for i in range(l - 1):
        if cubes[0] >= cubes[-1] and last >= cubes[0]:
            last = cubes[0]
            cubes.pop(0)
        elif last >= cubes[-1]:
            last = cubes[-1]
            cubes.pop(-1)
        else:
            return ("No")
    if cubes[0] > last:
        return ("No")
    return ("Yes")

T = int(input())
for i in range(T):
    N = int(input())
    cubes = list(map(int, input().split()))
    print(piling_cubes(cubes))

#### Date and Time (2) ####

# (49) Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month, day, year = map(int, input().split())
day_of_week = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_of_week]
print(day_name.upper())

# (50) Time Delta
# !/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    diff = dt2 - dt1
    return (str(abs(int(diff.total_seconds()))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#### Exceptions (1) ####

# (51) Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)

#### Built-ins (3) ####

# (52) Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
lista = []
for i in range(X):
    a = list(map(float, input().split()))
    lista.append(a)

app = zip(*lista)
for j in range(N):
    total = 0
    for i in range(X):
        total += lista[i][j]
    number = total/X
    formatted_number = "{:.1f}".format(number)
    print(formatted_number)

# (53) Athlete Sort
# !/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().rstrip().split())))
    K = int(input())
    arr.sort(key=lambda x: x[K])

    for j in arr:
        for k in j:
            print(k, end=' ')
        print()

# (54) ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = str(input())
lc = ""
uc = ""
odd_digits = ""
even_digits = ""
for i in s:
    if i.islower() == True:
        lc += i
    elif i.isupper() == True:
        uc += i
    elif i.isdigit() == True:
        if int(i) % 2 == 1:
            odd_digits += str(i)
        else:
            even_digits += str(i)

lc = sorted(lc)
uc = sorted(uc)
odd_digits = sorted(odd_digits)
even_digits = sorted(even_digits)

res = ""
for i in lc:
    res += i
for i in uc:
    res += i
for i in odd_digits:
    res += i
for i in even_digits:
    res += i

print(res)

#### Python Functionals (1) ####

# (55) Map and Lambda Function
cube = lambda x: x ** 3 # complete the lambda function
def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return([])
    if n == 1:
        return([0])
    arr = [0]
    attual = 1
    arr.append(attual)
    for i in range(2, n):
        arr.append(sum(arr[i-2:i]))
    return(arr)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#### Regex and Parsing challenges (17) ####
# (56) Detect Floating Point Number
from re import search

n = int(input())

for i in range(n):
    print(search(r"^([\+\-]){0,1}\d*\.\d+$", input()) is not None)

# (57) Re.split()
import re
regex_pattern = r"[,.]"
print("\n".join(re.split(regex_pattern, input())))

# (58) Group(), Groups() & Groupdict()
import re
S = str(input())
var = False
for i in range(1, len(S)):
    if S[i].isalnum() == True:
        if S[i] == S[i - 1]:
            print(S[i])
            var = True
            break

if var == False:
    print(-1)

# (59) Re.findall() & Re.finditer()
import re
S = input()
pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

res = re.findall(pattern, S)
if len(res) >= 1:
    for i in res:
        print(i)
else:
    print(-1)

# (60) Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = str(input())
k = str(input())
var = False

for i in range(len(S)):
    m = re.search(fr'{k}', S[i:i+len(k)])
    if bool(m == None) == False:
        print((i, i+len(k)-1))
        var = True

if var == False:
    print((-1, -1))

# (61) Regex Substitution
import re
N = int(input())
for j in range(N):
    print(re.sub(r'( =?)&&(?= )', ' and', re.sub(r'( =?)\|\|(?= )', ' or', input())))

# (62) Validating Roman Numerals
regex_pattern = r"^(?=.)M{0,3}(CM|CD|D?C{0,3})(?:(L?(X){0,3})|(XC)|(XL))?(IX|IV|V?I{0,3})$"
# ^(?=.) no 0
# M{0,3} matches all the 1000,2000,3000
# (CM|CD|D?C{0,3}) matches all the hundreds
# (?:(L?(X){0,3})|(XC)|(XL))? matches all the tens
# (IX|IV|V?I{0,3})$ matches all the units

# (63) Validating phone numbers
import re
N = int(input())
for _ in range(N):
    number = input()
    pattern = r"[7-9][0-9]{9}$"
    match = re.match(pattern, number)
    if match:
        print("YES")
    else:
        print("NO")

# (64) Validating and Parsing Email Addresses
import re
n = int(input())
pattern = r"[a-zA-Z0-9]+[a-zA-Z0-9_.\-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}+$"
for i in range(n):
    inp = input()
    match = re.match(pattern, inp.split()[1][1:-1])
    if match:
        print(inp)

# (65) Hex Color Code
import re
pattern=r"(#[a-fA-F0-9]{3,6})[^\n a-zA-Z0-9]"
N = int(input())
for _ in range(N):
    line = str(input())
    for i in re.findall(pattern, line):
        print(i)

# (66) HTML Parser - Part 1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

parser = MyHTMLParser()
N = int(input())
html = ""
for i in range(N):
    html += input()
parser.feed(html)

# (67) HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

# (68) Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

parser = MyHTMLParser()
N = int(input())
html = ""
for i in range(N):
    html += input()
parser.feed(html)

# (69) Validating UID
import re
T = int(input())
def UID_Validator(UID):
    if len(UID) != 10:
        return("Invalid")
    digits = re.findall(r"[0-9]", UID)
    if len(digits) < 3:
        return("Invalid")
    uppercase = re.findall(r"[A-Z]", UID)
    if len(uppercase) < 2:
        return("Invalid")
    pattern = r'^[a-zA-Z0-9]{10}'
    match = re.match(pattern, UID)
    if match == False:
        return("Invalid")
    if len(set(UID)) != len(UID):
        return("Invalid")
    return("Valid")

for i in range (T):
    UID = input()
    print(UID_Validator(UID))

# (70) Validating Credit Card Numbers
import re
N = int(input())
def same_string(cost):
    for i in cost:
        if i == cost[0]:
            continue
        else:
            return (False)
    return (True)
def validator(number):
    var = True
    if "-" in number:
        lista = [number.split("-")]
        for i in lista[0]:
            if len(i) != 4:
                return ("Invalid")
        number = ""
        for i in lista[0]:
            number += str(i)
    i = 0
    while i < (len(number) - 2):
        if same_string(number[i: i + 4]) == True:
            return ("Invalid")
        else:
            i += 1
    pattern = r"^[4-6]+[0-9]{15}$"
    match = re.match(pattern, number)
    if match:
        return ("Valid")
    else:
        return ("Invalid")

for _ in range(N):
    print(validator(input()))

# (71) Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
P = input()
print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# (72) Matrix Script
#!/bin/python3
import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string = ""
for i in range(m):
    for j in range(n):
        string += matrix[j][i]

print(re.sub(r"(?<=\w)[^a-zA-Z]+(?=\w)", " ", string))

#### XML (2) ####

# (73) XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    count = 0
    count += len(node.attrib)
    for i in node:
        count += get_attr_number(i)
    return(count)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# (74) XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#### Closures and Decorations (2) ####

# (75) Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key = lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# (76) Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        res = []
        for i in l:
            res.append(f"+91 {i[-10:-5]} {i[-5:]}")
        f(res)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

##### Numpy (15) ####

# (77) Arrays
import numpy
def arrays(arr):
    return(numpy.array(numpy.flip(arr), float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# (78) Shape and Reshape
import numpy

my_array = list(map(int, input().split()))
print(numpy.reshape(my_array, (3,3)))

# (79) Transpose and Flatten
import numpy
N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

print(numpy.transpose(arr))
print(numpy.array(arr).flatten())

# (80) Concatenate
import numpy
N, M, P = map(int, input().split())
arr1 = []
arr2 = []

for _ in range(N):
    arr1.append(list(map(int, input().split())))

for _ in range(M):
    arr2.append(list(map(int, input().split())))

print(numpy.concatenate((arr1, arr2), axis=0))

# (81) Zeros and Ones
import numpy

inpt = list(map(int, input().split()))
arr = numpy.array(inpt)
print(numpy.zeros(arr, dtype=int))
print(numpy.ones(arr, dtype=int))

# (82) Eye and Identity
import numpy
numpy.set_printoptions(legacy = '1.13')

N, M = map(int, input().split())
print(numpy.eye(N, M))

# (83) Array Mathematics
import numpy as n

N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append((list(map(int, input().split()))))
A = n.array(A, int)

for _ in range(N):
    B.append(list(map(int, input().split())))

B = n.array(B, int)
print(n.add(A, B))
print(n.subtract(A, B))
print(n.multiply(A, B))
print(A // B)
print(n.mod(A, B))
print(n.power(A, B))

# (84) Floor, Ceil and Rint
import numpy as n
n.set_printoptions(legacy='1.13')

arr = n.array(list(map(float, input().split())))
print(n.floor(arr))
print(n.ceil(arr))
print(n.rint(arr))

# (85) Sum and Prod
import numpy

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

fin = numpy.sum(arr, axis = 0)
print(numpy.prod(fin))

# (86) Min and Max
import numpy

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

print(numpy.max(numpy.min(arr, axis = 1)))

# (87) Mean, Var, and Std
import numpy
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(round(numpy.std(arr, axis =  None), 11))

# (88) Dot and Cross
import numpy
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

B = []
for i in range(N):
    B.append(list(map(int, input().split())))

print(numpy.dot(A, B))

# (89) Inner and Outer
import numpy

A = []
A.append(list(map(int, input().split())))
B = []
B.append(list(map(int, input().split())))

print(numpy.inner(A, B)[0][0])
print(numpy.outer(A, B))

# (90) Polynomials
import numpy

P = list(map(float, input().split()))
x = int(input())
print(numpy.polyval(P, x))

# (91) Linear Algebra
import numpy

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(float, input().split())))

print(round(numpy.linalg.det(arr), 2))


######## Algorithms (6) ########



#### Birthday Cake Candles (1)

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    # Write your code here
    counter = Counter(candles)
    maxx = candles[0]
    for i in candles:
        if i >= maxx:
            maxx = i
    return(counter[maxx])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()



#### Number Line Jumps (2)

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (x1 > x2) and (v1 >= v2):
        return("NO")
    if (x2 > x1) and (v2 >= v1):
        return("NO")
    if ((x1 > x2) and (v2 > v1)) or ((x2 > x1) and (v1 > v2)):
        # x1 + kv1 = x2 + kv2
        # x1 -x2 = k(v2 - v1)
        k = (x1 - x2) / (v2 - v1)
        pattern = "^(\d{0,}.0{1,})"
        match = re.search(pattern, str(k))
        if match or type(k) == int:
            return("YES")
        else:
            return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()



#### Viral Advertising (3)

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

people = [0, 5]

def people_day(n, a = 0):
    if n == 1:
        return (5)
    sum_people = 0
    sum_people += ((people_day(n - 1) // 2) * 3)
    people.append(sum_people)
    if a == 1:
        return(people)
    else:
        return(sum_people)

def viralAdvertising(n):
    # Write your code here
    if n == 1:
        return(2)
    pd = people_day(n, a = 1)
    app = []
    for i in pd:
        app.append(i//2)
    return(sum(app))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()



#### Insertion Sort - Part 1 (4)

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    element = arr[n-1]
    i = 2
    while arr[n-i] > element:
        arr[n-i+1] = arr[n-i]
        print(' '.join(map(str, arr)))
        i += 1
        if n-i == -1:
            break
    arr[n-i+1] = element
    print(' '.join(map(str, arr)))

            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)



#### Insertion Sort - Part 2 (5)

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    element = arr[n-1]
    i = 2
    while arr[n-i] > element:
        arr[n-i+1] = arr[n-i]
        i += 1
        if n-i == -1:
            break
    arr[n-i+1] = element
    return(arr)
    

def insertionSort2(n, arr):
    # Write your code here
    for i in range(2, n+1):
        arr_sorted = insertionSort1(i, arr[0:i])
        arr = arr_sorted + arr[i:]
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)



#### Recursive Digit Sum (6)

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k, nk = 0):
    # Write your code here
    if nk == 1:
        total = 0
        for i in n:
            total += (int(i)*k)
        return(superDigit(str(total), k, nk = 0))
    if len(n) == 1:
        return(n)
    else:
        total = 0
        for i in n:
            total += int(i)
        # print(total)
        return(superDigit(str(total), k, nk = 0))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k, nk = 1)

    fptr.write(str(result) + '\n')

    fptr.close()
    
