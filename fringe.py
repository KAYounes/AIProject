class PriorityQueue(object):

    def __init__(self):

        # List of items, flattened binary heap. The first element is not used.
        # Each node is a tuple of (value, priority, insert_counter)
        self.nodes = [None]  # first element is not used

        # Current state of the insert counter
        self.insert_counter = 0          # tie breaker, keeps the insertion order

    # Comparison function between two nodes
    # Higher priority wins
    # On equal priority: Lower insert counter wins
    def _is_higher_than(self, a, b):
        return b[1] > a[1] or (a[1] == b[1] and a[2] < b[2])

    # Move a node up until the parent is bigger
    def _heapify(self, new_node_index):
        while 1 < new_node_index:
            new_node = self.nodes[new_node_index]
            parent_index = new_node_index // 2
            parent_node = self.nodes[parent_index]

            # Parent too big?
            if self._is_higher_than(parent_node, new_node):
                break

            # Swap with parent
            tmp_node = parent_node
            self.nodes[parent_index] = new_node
            self.nodes[new_node_index] = tmp_node

            # Continue further up
            new_node_index = parent_index

    # Add a new node with a given priority
    def add(self, value, priority):
        new_node_index = len(self.nodes)
        self.insert_counter += 1
        self.nodes.append((value, priority, self.insert_counter))

        # Move the new node up in the hierarchy
        self._heapify(new_node_index)

    # Return the top element
    def peek(self):
        if len(self.nodes) == 1:
            return None
        else:
            return self.nodes[1][0]

    # Remove the top element and return it
    def pop(self):

        if len(self.nodes) == 1:
            raise LookupError("Heap is empty")

        result = self.nodes[1][0]

        # Move empty space down
        empty_space_index = 1
        while empty_space_index * 2 < len(self.nodes):

            left_child_index = empty_space_index * 2
            right_child_index = empty_space_index * 2 + 1

            # Left child wins
            if (
                len(self.nodes) <= right_child_index
                or self._is_higher_than(self.nodes[left_child_index], self.nodes[right_child_index])
            ):
                self.nodes[empty_space_index] = self.nodes[left_child_index]
                empty_space_index = left_child_index

            # Right child wins
            else:
                self.nodes[empty_space_index] = self.nodes[right_child_index]
                empty_space_index = right_child_index

        # Swap empty space with the last element and heapify
        last_node_index = len(self.nodes) - 1
        self.nodes[empty_space_index] = self.nodes[last_node_index]
        self._heapify(empty_space_index)

        # Throw out the last element
        self.nodes.pop()

        return result

    def inside(self, item):
        
        for indx in range(1, len(self.nodes)):
            if self.nodes[indx][0] == item:
                return indx
        return 0
    
    def replace(self, item):
        index = self.inside(item[0])
        if (index):
            item_cpy = (item[0], item[1], self.insert_counter + 1)
            self.nodes[index] = item_cpy
    
    def empty(self):
        return not (len(self.nodes) - 1)

    def display_queue(self, show_cost = True):
        temp = []
        for node in self.nodes:
            if (node is None):
                continue
            if(show_cost):
                temp.append([node[0].state, node[1]])
            else:
                temp.append(node[0].state)
                
                

        print(temp)


# pq = PriorityQueue()
# pq.add(1, 5)
# print(not pq.empty())
# pq.add(1, 5)
# pq.add(2, 5)
# pq.add(3, 5)
# print(pq.nodes)
# pq.replace((1,2))
# print(pq.nodes)