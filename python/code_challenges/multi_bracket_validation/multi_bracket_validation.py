'''
Required Features:
- [x] Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:
Round Brackets : ()
Square Brackets : []
Curly Brackets : {}
'''

from stacks_and_queues.stacks_and_queues import Stack

def multi_bracket_validation(input):
    '''
    Input: string  Output: boolean stating True if brackets are balanced in the input string
    '''

    bracket_tower = Stack()

    for char in input:
        if char in ['(','[','{']:
            bracket_tower.push(char)
        elif char in [')',']','}']:
            if bracket_tower.is_empty():
                return False
            removed_char = bracket_tower.pop()

            if char == ')' and removed_char != '(':
                return False
            elif char == ']'and removed_char != '[':
                return False
            elif char == '}' and removed_char != '{':
                return False

    if bracket_tower.is_empty():
        return True
    return False
