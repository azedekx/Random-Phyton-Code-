from collections import deque

class StackDeque:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack kosong"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return list(reversed(self.items))


if __name__ == "__main__":
    stack = StackDeque()

    stack.push("A")
    stack.push("B")
    stack.push("C")

    print("Isi stack (atas ke bawah):", stack.display())
    print("Elemen teratas:", stack.peek())
    print("Pop:", stack.pop())
    print("Isi stack setelah pop:", stack.display())
    print("Jumlah elemen:", stack.size())