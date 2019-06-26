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
from collections import defaultdict


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


def earliest_ancestor(family_tree, person):
    # default items are created using list(), which returns a new empty list object.
    family = defaultdict(list)

    # Creates a dictionary where each child (key) has parents (values)
    for parent, child in family_tree:
        family[child].append(parent)

    # If the child has no parents 🤷🏼‍♂️
    if person not in family:
        return -1

    # Perform DFS using the specified ID and the family list
    earliest = dfs(person, family)

    return earliest
