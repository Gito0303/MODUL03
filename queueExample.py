class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

    def offer(self, item):
        self.items.append(item)

    def poll(self):
        if self.empty():
            return None
        return self.items.pop(0)

    def element(self):
        if self.empty():
            return None
        return self.items[0]

    def peek(self):
        if self.empty():
            return None
        return self.items[0]

    def empty(self):
        return len(self.items) == 0


def queueExample():
    queue = Queue()
    queue.add("Java")
    queue.add("DotNet")
    queue.offer("PHP")
    queue.offer("HTML")
    print("remove : " + queue.remove())
    print("elements : " + queue.element())
    print("poll : " + str(queue.poll()))
    print("peek : " + str(queue.peek()))


queueExample()