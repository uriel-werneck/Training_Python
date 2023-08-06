# dictionary containing the vertices and their connections
vertices = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

# dictionary containing the status of each vertex
status = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 1
}

# lists that will receive the vertices
queue = []
processed = []

# creates the function that performs the Breadth-First Search
def breadth_first_search(vertices, status, node):

    queue.append(node)  # puts the initial vertex in the queue
    status[node] = 2  # changes the status of the initial vertex to 2

    while queue:  # while there are elements in the queue
        first = queue.pop(0)  # remove the first element from the queue
        processed.append(first)  # adds the first element to the precessed list
        status[first] = 3  # changes the status of the first element to 3

        for neighbor in vertices[first]:  # for each neighbor of the first element in the queue
            if status[neighbor] == 1:  # if the status of the neighbor is equal to 1
                queue.append(neighbor)  # add the neighbor to the end of the queue
                status[neighbor] = 2  # change the status of the neighbor to 2

            elif status[neighbor] == 2 or status[neighbor] == 3:  # if the status of the neighbor is equal to 2 or 3
                continue  # ignore this neighbor

# calls the function that performs the Breadth-First Search
breadth_first_search(vertices, status, 'A') # vertex "A" is defined as the initial node

# displays the result of the Breadth-First Search
print('Result of Breadth-First Search:')
print(processed)
