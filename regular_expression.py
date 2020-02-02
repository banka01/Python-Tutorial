# text = 'welcome'
# if 'a' in text:
#     print('vowel')
# elif 'e' in text:
#     print('vowel e')

import re
#re.search(pattern,string,flag)
## pattern :  should be raw string

pattern = r'Welcome\nRegular'
print(pattern)
print(r'C:\\')
sample_string = 'Regular expression'
obj = re.search(r'e',sample_string)
print(obj)
print(re.search(r'E',sample_string))
print(re.search(r'n',sample_string))
print(re.search(r'an',sample_string))
print(re.search(r'ar',sample_string))
print(sample_string[5:7])
pancard = r'NBCDE1111X'
print(re.search(r'.',pancard))    # . matched any character except newline
string = 'BNG.CITY'
print(re.search(r'\.',string))
string = 'ABC'
obj = re.search(r'\*',string)
if obj:
    print('given string contains *')
else:
    print('given string does not contain *')

print(re.search(r'ann123','anan1234'))

## character class
#'[]' character class
print(re.search(r'[cab]','aRepublic day'))
print(re.search(r'[aeiou]','Republic day'))
print(re.search(r'[a-z]','26'))
print(re.search(r'[a-z]','26January'))
print(re.search(r'[a-zA-Z]','26January'))
print(re.search(r'[a-zA-Z0-9]','26January'))
print(re.search(r'[a-gop]','f12'))
print(re.search(r'[a-gop]','p12'))
print(re.search(r'[a-gop]','x12'))
print(re.search(r'[^abc]','efgh')) ## inside a character clas ^ means negate
print(re.search(r'[^abc]','abd'))
print(re.search(r'[^abc]','bc'))

# Anchors :
# ^ : match at the start of the string
print(re.search(r'Republic','Today is Republic Day'))
print(re.search(r'^Republic','Today is Republic Day'))
print(re.search(r'^Republic','Republic Day is on 26th Jan'))

## $ : at the end
print(re.search(r'day','Republic day is on 26th Jan'))
print(re.search(r'day$','Today is Sunday '))

# word boundary. \b
print(re.search(r'day','Today is Sunday '))

print(re.search(r'\bday\b','Today is Rainy  day '))

# quantifier
# * : zero or more time of the preceding pattern
print(re.search(r'ab*','abcd')) ## b* , b, bb, bbb, bbbbbb ,bbbbbbb
print(re.search(r'ab*','abbbcd')) # a, ab, abb, abbbbb,abbbbbbcd
print(re.search(r'ab*','acd'))
print(re.search(r'ab*','abbbbbbbbbbcd'))
print(re.search(r'ab*c','abbbbbbbbbbcd')), # ac, abc, abbbbc, abbc, abbbbbbbbc
print(re.search(r'ab*c','abbbbbbbbbbd'))
print(re.search(r'ab*c','acccd'))

# + : one or more occur
print(re.search(r'ab+c','abcccd'))
print(re.search(r'ab+c','acccd'))
print(re.search(r'Ab+cd*','Abcd'))

# ? : zero or 1 times
print(re.search(r'ab?c','abc'))
print(re.search(r'ab?c','ac'))
print(re.search(r'ab?c','abbc'))

## {m,n}
print(re.search(r'ab{2,5}c','abbc'))
print(re.search(r'ab{2,5}c','abbbbbbbbc'))
#{m,}
#{m}
print(re.search(r'[0-9]{4}','202'))
#{,m}

## \d -- it only matches as digit [0-9]
##match a year
print(re.search(r'\d+','22'))
## DD-MM-YYYY
# D-M-YYYY
print(re.search(r'\d{1,2}\-\d{1,2}\-\d{4}','01-02-2020'))
print(re.search(r'\d{1,2}\-\d{1,2}\-\d{4}','01-02-20'))

# word character , [0-9a-zA-z_],
## Feb 02
print(re.search(r'[0-9a-zA-Z_]+','Feb02'))
print(re.search(r'\w+','Feb 02'))

# space, \s, [\t\r\n]

print(re.search(r'\w+\s+\w+','Feb FE'))

## \D ,non digit , [^0-9]
print(re.search(r'\D+','Feb 02'))

#\S, non whitespace
print(re.search(r'\S+','Feb 02123'))

print(re.search(r'\d+','Feb 02123'))

#\W, anything which is not a wordchar
print(re.search(r'\W+','1234'))

## DD-MM-YYYY
obj = re.search(r'\d{1,2}\-\d{1,2}\-\d{4}','Todays date is 01-02-2020')
print(obj.group())
print(type(obj.group()))
if obj:
    print('input date is legal')
else:
    print('input is illegal')

## ((a))
obj = re.search(r'(\d{1,2})\-(\d{1,2})\-(\d{4})','Todays date is 01-02-2020')
if obj:
    day,month,year = obj.groups()
    print(f"day is {day}, month is {month}, year is {year}")

obj1 = re.search(r'((\d{1,2})\-(\d{1,2})\-(\d{4}))','Todays date is 01-02-2020')
if obj1:
    date, day,month,year = obj1.groups()
    print(f"day is {day}, month is {month}, year is {year},date is {date}")
    print(obj1.groups())
print(obj.group(0))
print(obj.group(1))
print(obj.group(2))

print(re.search(r'abc\s+\d+','ABC 23',re.IGNORECASE))
##re.VERBOSE

obj = re.search(r'[0-9]+' 
                r'[a-z]' # only alpha
                ,'123abc',re.VERBOSE)
print(obj)

text = 'city BNG  MYS KOL'
obj = re.finditer(r'\w+',text)
if obj:
    for x in obj:
        print(x.group())
