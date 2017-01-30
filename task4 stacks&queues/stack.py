class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):  # положить элемент в стек
        self.items.append(item)

    def pop(self):  # удалить элемент из стека и вернуть его значение
        return self.items.pop()

    def peek(self):  # вернуть значение последнего элемента стека (не удаляя его)
        return self.items[-1]

    def isEmpty(self):  # вернуть True, если стек пуст, иначе вернуть False
        return self.items == []