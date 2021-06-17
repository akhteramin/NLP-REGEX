import re

# \b returns a match where the specified pattern is at the beginning or at the end of a word.
x = re.findall(r"tory\b", "hello there this is my reporsitory")
print(x)
# ['tory']

# \d returns a match where the specified pattern is at the beginning or at the end of a word. Adding '+' (\d+) will return grouped string.
x = re.findall(r"\d", "hello there this is my reporsitory published in 2021")
print(x)
# ['2', '0', '2', '1']

x = re.findall("\d+", "hello there this is my reporsitory published in 2021")
print(x)
# ['2021']

# the capital expression "\D" returns the text not including digits
x = re.findall("\D+", "hello there this is my reporsitory published in 2021")
print(x)
# ['hello there this is my repository published in ']

# \w helps in extraction of alphanumeric characters only (characters from a to Z, digits from 0-9, and the underscore _ character)
x = re.findall("\w+","hello there this is my repository published in 2021. The name is code_victor")
print(x)
# ['hello', 'there', 'this', 'is', 'my', 'repository', 'published', 'in', '2021', 'The', 'name', 'is', 'code_victor']

# \W returns match at every non-alphanumeric character. Basically opposite of \w.
x = re.findall("\W+","hello there this is my repository published in 2021. The name is code_victor !")
print(x)
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '. ', ' ', ' ', ' ', ' !']

