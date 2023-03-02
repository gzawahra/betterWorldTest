# test_chain is a function that keeps track of parenthesis to make sure they are well formed,
# ie. (each parentheses has a closing counter part).
#
# The time complexity of the test_chain function is O(n), n being the length of the given string of parentheses.
# In the worst case, the function will iterate through all the characters in the string, and push each one onto 
# the stack if all parentheses are openning or pop them off if they are all closing .
#
# In the best case, the function will iterate through the characters once and perform constant time operations 
# for each character, leading to O(n) time complexity ie. (empty string or well formed).
#
# Therefor time complexity of the test_chain function depends on the input size, 
# which means that the time complexity is linear with the order O(n).

def test_chain(s: str) -> bool:
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


############### function test ###############

# Well formed
print("Well formed")
print(f"() : is {test_chain('()')}")
print(f"()()()()() : is {test_chain('()()()()()')}")
print(f"((((()()())))) : is {test_chain('((((()()()))))')} ")
print(f"((())) : is {test_chain('((()))')}")
print(f"empty String : is {test_chain('')} ")
print(f"space: is {test_chain(' ')} ")


# Ill formed
print("Ill formed")
print(f")( : is {test_chain(')()')}")
print(f"()())(()() : is {test_chain('()())(()()')}")
print(f"(((()()()()()())))) : is {test_chain('(((()()()()()()))))')}")
print(f"(((())))) : is {test_chain('(((()))))')}")
print(f"( : is {test_chain('(')}")
