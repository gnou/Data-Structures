# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    ignore_final_check = False
    for i, character in enumerate(text):
        if i == len(text) - 1:
            finished_enumeration = True
        if character == '(' or character == '[' or character == '{':
            # push stack
            bracket = Bracket(character, i)
            opening_brackets_stack.append(bracket)
        if character == ')' or character == ']' or character == '}':
            if len(opening_brackets_stack) == 0:
                ignore_final_check = True
                print(i + 1)
                break
            else:
                top = opening_brackets_stack[-1]
                del opening_brackets_stack[-1]

                if not top.match(character):
                    ignore_final_check = True
                    print(i + 1)
                    break

    if not ignore_final_check:
        if len(opening_brackets_stack) == 0:
            print("Success")
        else:
            top = opening_brackets_stack[-1]
            print(top.position + 1)
