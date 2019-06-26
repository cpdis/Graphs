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


def dfs(starting_vertex, family):
    # Depth first search uses stacks so...
    # Create a stack
    stack = Stack()
    stack.push([starting_vertex])

    # Create an array for visited vertices
    visited = []

    while stack.size() > 0:
        path = stack.pop()

        # Get the last vertex in the path
        vertex = path[-1]

        # Check if the vertex has been visited or not
        if vertex not in visited:
            visited.append(vertex)

        for descendant in family[vertex]:
            new_path = path.copy()
            new_path.append(descendant)
            stack.push(new_path)

    return visited[-1]
