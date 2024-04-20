from stack import Stack


def balanced_brackets(brackets_string: str) -> None:
    brackets_correspond = {')': '(',
                           ']': '[',
                           '}': '{'}

    brackets_stack = Stack()
    for bracket in brackets_string:
        if bracket in brackets_correspond.values():
            brackets_stack.push(bracket)
        elif bracket in brackets_correspond.keys():
            if not brackets_stack.is_empty() and brackets_correspond[bracket] == brackets_stack.peek():
                brackets_stack.pop()
            else:
                return 'Несбалансированно'

    if brackets_stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


def main() -> None:
    brackets_set = input()
    print(balanced_brackets(brackets_set))


if __name__ == '__main__':
    main()