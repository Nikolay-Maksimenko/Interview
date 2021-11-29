BRACKETS = {'(': ')', '[': ']', '{': '}'}

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        lenght = self.size()
        if lenght == 0:
            return True
        else:
            return False

    def push(self, new_element):
        return self.stack.append(new_element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        lenght = self.size()
        if lenght != 0:
            return self.stack[lenght - 1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def check_balance(self, string):
        if len(string) != 0:
            for symbol in string:
                if symbol in BRACKETS.keys():
                    self.push(symbol)
                elif symbol in BRACKETS.values():
                    if symbol == BRACKETS.get(self.peek()):
                        self.pop()
                    else:
                        return 'Несбалансированно'
            if self.isEmpty():
                return f'Сбалансированно'
            else:
                return 'Несбалансированно'
        else:
            return 'Пустая строка'

string = '[([])((([[[]]])))]{()}'
stack_obj = Stack()
print(stack_obj.check_balance(string))