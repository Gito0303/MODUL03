class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def search(self, item):
        try:
            index = self.items[::-1].index(item)
            return len(self.items) - index
        except ValueError:
            return -1

at = Stack()

at.push("Aku")
at.push("Anak")
at.push("Indonesia")

print("Next : " + at.peek())
at.push("Raya")
print(at.pop())
at.push("!")

count = at.search("Aku")
while count != -1 and count > 1:
    at.pop()
    count -= 1

print(at.pop())
print(at.empty())
