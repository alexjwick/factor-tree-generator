import math

treeHeight: int = 0

class Node:
    def __init__(self, val: int, depth: int):
        self.left: Node = None
        self.right: Node = None
        self.val: int = val
        self.depth: int = depth

def generateFactorTree(node: Node) -> Node:
    node: Node = node

    global treeHeight

    if node.val == 0:
        treeHeight = 1
        return node
    elif node.val < 0:
        node.left = Node(-1, node.depth + 1)
        node.right = generateFactorTree(Node(-1 * num, node.depth + 1))
        return node
    else:
        for i in range(2, int(node.val/2)):
            if node.val % i == 0:
                node.left = Node(i, node.depth + 1)
                node.right = generateFactorTree(Node(int(node.val / i), node.depth + 1))
                return node
        treeHeight = node.depth + 1
        return node

def printFactorTree(root: Node) -> None:
    root: Node = root

if __name__ == '__main__':
    while True:
        i: str = input("Enter integer: ")
        if(i != "exit"):
            isInt: bool = True
            try:
                num: int = int(i)
            except ValueError:
                isInt = False
            if isInt:
                root: Node = generateFactorTree(Node(num, 0))
                print(treeHeight)
                treeHeight = 0
            else:
                print("Input must be an integer")
        else:
            break