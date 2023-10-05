# N174

# def least_divider(a, b):
#     if b == 0:
#         return a
#     else:
#         return least_divider(b, a % b)

# print(least_divider(48, 36))

#N176

# def shifr(word):
#     alphabet = {
#         'A': 'Alpha', 
#         'B': 'Brav',
#         'C': 'Charlie',  
#         'D': 'Delta',  
#         'E': 'Echo',  
#         'F': 'Foxtrot',
#         'G': 'Golf',
#         'H': 'Hotel',  
#         'I': 'India',  
#         'J': 'Juliet',
#         'K': 'Kilo', 
#         'L': 'Lima',
#         'M': 'Mike',
#         'N': 'November',
#         'O': 'Oscar',
#         'P': 'Papa',
#         'Q': 'Quebec',
#         'R': 'Romeo',
#         'S': 'Sierra',
#         'T': 'Tango',
#         'U': 'Uniform',
#         'V': 'Victor',
#         'W': 'Whiskey',
#         'X': 'Xray',
#         'Y': 'Yankee',
#         'Z': 'Zulu',
#     }

#     if word == '':
#         return ''
#     else:
#         return alphabet[word[0].upper()] + ' ' + shifr(word[1:])
    
# print(shifr('Hello'))

# N177

# def func(roman):
#     tablet = {
#         'M': 1000, 
#         'D': 500,
#         'C': 100,
#         'L': 50,
#         'X': 10,
#         'V': 5,
#         'I': 1,
#     }

#     if roman == '':
#         return 0
#     elif len(roman) == 1:
#         return tablet[roman]
#     else:
#         n1 = tablet[roman[0]]
#         n2 = tablet[roman[1]]
#         if n1 < n2:
#             return n2 - n1 + func(roman[2:])
#         else:
#             return n1 + n2 + func(roman[2:])

# print(func('XCIX'))

# def ispalindrome(word):
    
#     test = word.lower()

#     if test == '':
#         return True
#     elif len(test) == word.count(test[0]):
#         return True
#     elif test[0] == test[-1]:
#         return ispalindrome(word[1:len(word)-1])
#     else:
#         return False
    
# enter = input("Enter a word: ")

# print(ispalindrome(enter))

# N179

# def sqrt(n, guess=1):

#     if abs(n - guess ** 2) <= 10 ** -12:
#         return guess
#     else:
#         return sqrt(n , (guess + n/guess)/2)

# print(sqrt(2))

# N180


# def func(s, t):

#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[-1] != t[-1]:
#             cost = 1
#         d1 = func(s[:-1], t) + 1
#         d2 = func(s, t[:-1]) + 1
#         d3 = func(s[:-1], t[:-1]) + cost

#         return min(d1, d2, d3)
    
# print(func('kitten', 'sitting'))

# N186

# letters = ["A", "A", "A", "A", "A", "A", "A", "A", "A",
# "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A"]

# def func(mylist, count=1):

#     if mylist == '':
#         return []
#     elif len(mylist) == 1:
#         return [mylist[0]] + [count]
#     if mylist[0] != mylist[1]:
#         return [mylist[0]] + [count] + func(mylist[1:], count=1)
#     else:
#         return func(mylist[1:], count+1)
    
# print(func(letters))
