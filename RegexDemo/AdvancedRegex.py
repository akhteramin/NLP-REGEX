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


# Operator Precedence Hierarchy for regular expression
# 1. Parenthesis ()
# 2. Counters * + ? {}
# 3. Sequences and Anchors -- the ^my end$
# 4. Disjunction |

# /[a-z]*/ matches zero or more letters. Regex always tend to match the largest string. This pattern is called greedy

# /*?/ or /+?/ matches zero or more letters. This regex tend to match as little string as possible. This pattern is called non-greedy

# Simple patterns
x = re.findall("[tT]he","the theory theology")
print(x)
#['the', 'the', 'the']

# Strictly define the length of matching using word boundary

x = re.findall("(\b[tT]he\b)","The the theology")
print(x)

#['the', 'the'] --> theology is not included

# Now if we want to specify that we instances in which there are not alphabetic letters on either side of "T/the"

x = re.findall("[^a-zA-Z][tT]he[^a-zA-Z]","he is the man.")
print(x)
# ['the']

#But it wont find the line begins with "T/the"
x = re.findall("[^a-zA-Z][tT]he[^a-zA-Z]","The boy want to be a good man.")
print(x)
# []

# This might resolve the issue.
x = re.findall('((^|[^a-zA-Z])?[tT]he([^a-zA-Z]|$))',"the boy want to be a good man.")
print(x)

#[('the ', '', ' ')]

# The process we have just gone through was based on fixing two kinds of errors:
# false positive(strings that we incorrectly matched) -- Precision
# false negative(strings that we incorrectly missed) -- Recall

## More Operators

# Aliases for common set of Regex
# \d : [0-9]
# \D : ^[0-9]
# \w : [a-zA-Z0-9_] -- AlphaNumeric+Underscore
# \W : ^[a-zA-Z0-9_]
# \s : [ \r\t\n\f] -- whitespace (space, tab)
# \S : ^[ \r\t\n\f] -- whitespace (space, tab)


# Regex for counting
# * : zero or more occurrences of previous operators or expression
# + : one or more occurrences of previous operators or expression
# ? : exactly zero or one occurrences of previous operators or expression
# {n} : exactly n occurrences of previous operators or expression
# {n,m} : from n to m occurrences of previous operators or expression
# {n,} : at least n occurrences of previous operators or expression
# {,m} : up to m occurrences of previous operators or expression

# /{3}/ means exactly 3 occurrences of the previous character or expression. For instance: /a.{24}z/-- 'a' followed by 24 dots followed by z



# Complex Examples
# "Any machine with at least 6 GHz and 500 GB of disk space for less than $1000". TO do this retrieval we need to do as follows:

x = re.findall("\$[0-9]+","This is a $300 dollar mac book.")
print(x)
# ['$300']

#But to handle cents we need to do this:
x = re.findall("\$[0-9]+\.[0-9][0-9]","This is a $300.66 dollar mac book.")
print(x)
# ['$300.66']

#The pattern only allow /$300.45/ not /$300/. Now we need to make the cents optional.
x = re.findall("(\$[0-9]+(\.[0-9][0-9])?\\b)","this is a $300.04 dollar mac.")
print(x)
# [('$300.04', '.04')]

# We need limit numbers before decimal will be 3 so that it would not align 4-5 numbers. Here $3000 or $1000 (<$999) will not work.
x = re.findall("(\$[0-9]{3}(\.[0-9][0-9])?\\b)","this is a $300.04 dollar mac.")
print(x)
# [('$300.04', '.04')]

# Let mae some regex to identify the disk space 5 GB or Gigabytes

x = re.findall("\\b([0-9]+(\.[0-9]+)? *(GB|[Gg]igabytes) \\b)","this is a PC having 10 Gigabytes disk.")
print(x)

#[('10 Gigabytes ', '', 'Gigabytes')]

# ---------------------Substitution, Capture Groups ---------------------------
