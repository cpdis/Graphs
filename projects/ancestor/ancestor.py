'''
Earliest Ancestor
------------------
Main problem statement: Write a function that, given the dataset and the ID of an 
individual in the dataset, returns their earliest known ancestor – the one at the 
farthest distance from the input individual. If there is more than one ancestor tied 
for "earliest", return the one with the lowest numeric ID. If the input individual 
has no parents, the function should return -1.

Process: I think this will be a good place to use depth first search (DFS) and stacks.
A Stack class can be based on previous assignments as well as the DFS implementation. A
earliest_ancestor method will need to be written to actually implement the logic provided
in the problem statement.
'''


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
