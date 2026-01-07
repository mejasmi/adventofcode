"""Algorithm Approach
The best algorithm for this problem is Kruskal's Algorithm with Union-Find (Disjoint Set Union):
High-Level Steps:

Calculate all pairwise distances between junction boxes

For n junction boxes, you'll have n(n-1)/2 possible connections
Distance formula: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)


Sort all edges by distance (ascending order)
Use Union-Find data structure to track connected components:

Each junction box starts as its own component
Union-Find allows efficient merging and checking if boxes are already connected


Process edges in order (Kruskal's algorithm):

For each edge (shortest first):

Check if the two junction boxes are already in the same component
If not, connect them (union operation)
If yes, skip (they're already connected)


Stop after making 1000 connections


Find component sizes:

After 1000 connections, determine the size of each connected component
Find the three largest components
Multiply their sizes together



Key Data Structures:
Union-Find (Disjoint Set Union):
- parent[i]: parent of node i
- size[i]: size of component containing i (if i is root)

Operations:
- find(x): Find root of x's component (with path compression)
- union(x, y): Merge components containing x and y
Pseudocode:
1. Parse input to get list of junction box coordinates
2. Create list of all edges with distances
3. Sort edges by distance
4. Initialize Union-Find with n junction boxes
5. connections_made = 0
6. For each edge in sorted order:
     if connections_made == 1000: break
     if find(edge.box1) != find(edge.box2):
         union(edge.box1, edge.box2)
         connections_made++
7. Count component sizes
8. Find 3 largest sizes and multiply them
Complexity:

Time: O(n² log n) for sorting all edges
Space: O(n²) for storing all edges"""


from collections import deque    
import numpy as np

# file_path = "data/test_d8.txt"

file_path = "data/input_day8.txt"

FIRST_PART = True
MAX_CONNECTIONS = 1000

# class for Union-Find
class UnionFind(object):
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # Find root with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Union by size
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        # Attach smaller tree under larger tree
        if self.size[root_x] > self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        
        return
    
    def get_component_sizes(self):
        # get size of each component
        component_sizes = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in component_sizes:
                component_sizes[root] = self.size[root]
        return list(component_sizes.values())


if __name__ == "__main__":

    with open(file=file_path, mode="r+") as file:
        lines = file.readlines()
        
        junction_boxes = []
        for line in lines:
            x, y, z = map(int, line.strip().split(','))
            junction_boxes.append((x,y,z))

        # calculate Eucledian distance
        n = len(junction_boxes)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                x1, y1, z1 = junction_boxes[i]
                x2, y2, z2 = junction_boxes[j]
                distance = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
                edges.append((distance, i, j))

        # sort the edges by distance
        edges.sort()
        

        if FIRST_PART:
            uf = UnionFind(n)

            connections_made = 0
            # connect edges
            for distance, i, j in edges:
                if connections_made == MAX_CONNECTIONS:
                    break
                uf.union(i, j)
                connections_made += 1
            
            # Get component sizes
            component_sizes = uf.get_component_sizes()
            component_sizes.sort(reverse=True)

            # Multiply three largest
            result = component_sizes[0] * component_sizes[1] * component_sizes[2]

            print("Result is: ",result,".")

        else:
            pass