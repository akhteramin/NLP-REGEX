# NLP-REGEX
This repository contains a large range of regular expression that is required in Natural Language Processing.

# Operator Precedence Hierarchy for regular expression
1. Parenthesis ()
2. Counters * + ? {}
3. Sequences and Anchors -- the ^my end$
4. Disjunction |

## More Operators

# Aliases for common set of Regex
\d : [0-9]
\D : ^[0-9]
\w : [a-zA-Z0-9_] -- AlphaNumeric+Underscore
\W : ^[a-zA-Z0-9_]
\s : [ \r\t\n\f] -- whitespace (space, tab)
\S : ^[ \r\t\n\f] -- whitespace (space, tab)


# Regex for counting
* : zero or more occurrences of previous operators or expression
+ : one or more occurrences of previous operators or expression
? : exactly zero or one occurrences of previous operators or expression
{n} : exactly n occurrences of previous operators or expression
{n,m} : from n to m occurrences of previous operators or expression
{n,} : at least n occurrences of previous operators or expression
{,m} : up to m occurrences of previous operators or expression

/{3}/ means exactly 3 occurrences of the previous character or expression. For instance: /a.{24}z/-- 'a' followed by 24 dots followed by z

Please note that in python, word boundary will work with "\b". Rather we need to use this "\\b" to apply word boundary in regex.
