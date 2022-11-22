import math

class Node:
    def __init__(self, val: int, level: int):
        self.left: Node = None
        self.right: Node = None
        self.val: int = val
        self.level: int = level

def generateFactorTree(node: Node) -> Node:
    node: Node = node
    if node.val == 0:
        return node
    elif node.val < 0:
        node.left = Node(-1, node.level + 1)
        node.right = generateFactorTree(Node(-1 * num, node.level + 1))
        return node
    else:
        for i in range(2, int(math.sqrt(node.val))):
            if node.val % i == 0:
                node.left = Node(i, node.level + 1)
                node.right = generateFactorTree(Node(node.val / i, node.level + 1))
                return node
        return node

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
                generateFactorTree(Node(num, 0))
            else:
                print("Input must be an integer")
        else:
            break