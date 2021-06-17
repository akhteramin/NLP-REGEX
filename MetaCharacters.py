import re

# (.) matches any character (except newline character)
x = re.findall("re.","I published a research paper this year.")
print(x)

x = re.findall("re..","I published a research paper this year.")
print(x)

x = re.findall("re...","I published a research paper this year.")
print(x)


x = re.findall("re....","I published a research paper this year.")
print(x)


x = re.findall("re.....","I published a research paper this year.")
print(x)


x = re.findall("re......","I published a research paper this year.")
print(x)
# ['res']
# ['rese']
# ['resea']
# ['resear']
# ['researc']
# ['research']
# -----------------------------------------------------------------------
# (^) starts with
# It checks whether the string starts with the given pattern or not.

x = re.findall("^Data", "Dataset is required")
print(x)
# ['Data']
# -----------------------------------------------------------------------

# ($) ends with
# It checks whether the string ends with the given pattern or not.
x = re.findall("now$", "Dataset is important now")
print(x)
# ['now']
# -----------------------------------------------------------------------
# (*) matches for zero or more occurrences of the pattern to the left of it
#Check if the string contains "da" followed by 0 or more "a" characters and ending with y
x = re.findall("da*a", "daaa daa daaaa")
print(x)
# ['daaa', 'daa', 'daaaa']

# (+) matches for one or more occurrences of the pattern to the left of it
#Check if the string contains "da" followed by one or more "a" characters and ending with y
x = re.findall("da+a", "daaa da daaaa")
print(x)
# ['daaa', 'daaaa']

# (?) matches zero or one occurrence of the pattern left to it.
x = re.findall("eas?y","easy, eay, easssy")
print(x)
# ['easy', 'eay']

# | either or -- this is called pipe operator
x = re.findall("data|research", "My research is based on the data collected during experiment.")
print(x)
# ['research', 'data']

