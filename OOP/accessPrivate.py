class Queue:
    def __init__(self, contents):
        self.__hiddenlist = list(contents)

    def push(self, value):
        self.__hiddenlist.insert(0, value)

    def pop(self):
        return self.__hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self.__hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
# Leading double underscore tell python interpreter to rewrite name in order to avoid conflict in subclass.
# Interpreter changes variable name with class extension and that feature known as the Mangling
print(queue._Queue__hiddenlist)