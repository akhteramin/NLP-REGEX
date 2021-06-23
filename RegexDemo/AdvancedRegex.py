import re

# Use of Bracket specifies disjunction of characters
x = re.findall("[abcd]","hello there this is my repository published in 2021. The name is code_victor !")
print(x)

#['b', 'd', 'a', 'c', 'd', 'c']

# Only Upper case letters

x = re.findall("[A-Z]","hello there this is my repository published in 2021. The name is code_victor !")

print(x)

#['T']

# Exception sign is here "^"
x = re.findall("[^A-Z]","hello there this is my repository published in 2021. The name is code_victor !")
print(x)

# ['h', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e', ' ', 't', 'h', 'i', 's', ' ', 'i', 's', ' ', 'm', 'y', ' ', 'r', 'e', 'p', 'o', 's', 'i', 't', 'o', 'r', 'y', ' ', 'p', 'u', 'b', 'l', 'i', 's', 'h', 'e', 'd', ' ', 'i', 'n', ' ', '2', '0', '2', '1', '.', ' ', 'h', 'e', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'c', 'o', 'd', 'e', '_', 'v', 'i', 'c', 't', 'o', 'r', ' ', '!']

x = re.findall("[^Ss]","I have no excuisite reason for it.")

print(x)

# ['I', ' ', 'h', 'a', 'v', 'e', ' ', 'n', 'o', ' ', 'e', 'x', 'c', 'u', 'i', 'i', 't', 'e', ' ', 'r', 'e', 'a', 'o', 'n', ' ', 'f', 'o', 'r', ' ', 'i', 't', '.']

# It is called Kleene*. It commonly refers to "zeros or more occurrences of immediately previous character or Regex."
# zeros or more 'a's or 'b's
x = re.findall("[ab]*","abababab aaaaa bbbbb")

print(x)
#['abababab', '', 'aaaaa', '', 'bbbbb', '']

# Kleene+: "one or more occurrences of immediately previous character or Regex"
# [0-9]+ is a normal way to specify the sequence.
x = re.findall("[0-9]+","abababab aaaaa bbbbb 2019 2020 1111")

print(x)
# ['2019', '2020', '1111']

# "." is a wild card expression. To specify any character is allowed here.
x = re.findall("beg.n","begin begnn begun beugn")

print(x)

#['begin', 'begnn', 'begun']

# Using wild card and Kleene* together. This refers to "any string character is allowed in between."
x = re.findall("beg.*n","begiiiin ")
print(x)
x = re.findall("beg.*n","begabcdsn ")
print(x)
x = re.findall("beg.*n","beguasdfn ")
print(x)
x = re.findall("beg.*n","beugfdsadfn ")
print(x)

# ['begiiiin'] ['begabcdsn'] ['beguasdfn'] []

# Caret "^" has three uses: (1) to match the start of the line (2) dictate negation inside of square brackets (3) just to mean a caret
x = re.findall("^The dog.*\.$","The dog is loyal.")
print(x)

# ['The dog is loyal.']

# Disjunction operator: pipe(|)
x = re.findall("cat|dog","The dog is loyal. But cat is not.")
print(x)

# ['dog', 'cat']

# Parenthesis operator: ( ). This operator will be used to match both "my" and "mine"

x = re.findall("(m(y|ine))","my world is not mine anymore.")
print(x)

# [('my', 'y'), ('mine', 'ine')]

# Match these: Column 1, Column 2, Column 3. Below is the whole pattern repeated zero or more times.
x = re.findall("(Column [0-9]+ *)*","Column 1 Column 2 Column 3")
print(x)