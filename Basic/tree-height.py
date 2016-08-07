# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
        def __init__(self, data):
                self.data = data
                self.children = []

        def add_child(self, obj):
                self.children.append(obj)

        def height(self):
            if len(self.children) == 0:
                return 1
            else:
                children_height = []
                for child in self.children:
                    children_height.append(child.height())
                return max(children_height) + 1

class Tree:
        def read(self):
            self.n = int(sys.stdin.readline())

            self.nodes = []
            for num in range(self.n):
                node = Node(num)
                self.nodes.append(node)

            self.parents = list(map(int, sys.stdin.readline().split()))
            for index, parent in enumerate(self.parents):
                node = self.nodes[index]
                if parent != -1:
                    parent_node = self.nodes[parent]
                    parent_node.add_child(node)
                else:
                    self.root = node

        def compute_height(self):
            return self.root.height()


class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

def main():
  tree = Tree()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
