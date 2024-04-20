class Stack:
    def __init__(self) -> None:
        self.stack_list = []

    def is_empty(self) -> bool:
        if not self.stack_list:
            return True
        else:
            return False

    def push(self, element) -> None:
        self.stack_list.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack_list.pop(-1)

    def peek(self):
        if not self.is_empty():
            return self.stack_list[-1]

    def size(self) -> int:
        return len(self.stack_list)
