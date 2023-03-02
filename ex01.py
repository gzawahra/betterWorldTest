# find_wellformed_subchain is a functions that returns the length of the longest well
# formed chain of parentheses.

# Like the test_chain function the time complexity is o(n) n being the length of the 
# string and the space complexity is also O(n) since the stack in a worst case scenario
# must hold the totality of the input string. In the best case where the input string is 
# empty or composed of well-formed parentheses, the stack will hold only one element and 
# the space complexity will be O(1).

def find_wellformed_subchain(s: str) -> int:
    max_length = 0
    stack = [-1]
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length

############### function test ###############
print(f"(((()()()()()()))))((((()()()))))(((())))) : {find_wellformed_subchain('(((()()()()()()))))((((()()()))))(((()))))')}")
print(f"((((()()())))) : {find_wellformed_subchain('((((()()()))))')}")
print(f" empty string : {find_wellformed_subchain('')}")
print(f"(((((((((((((((((((( : {find_wellformed_subchain('((((((((((((((((((((')}")
print(f")))))))))))))))))))))))) : {find_wellformed_subchain('))))))))))))))))))))))))')}")
print(f")))))))))))))))()))))))))) : {find_wellformed_subchain(')))))))))))))))())))))))))')}")