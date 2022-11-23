import math

class Node:
    def __init__(self, val: int, depth: int):
        self.left: Node = None
        self.right: Node = None
        self.val: int = val
        self.depth: int = depth

def generateFactorTree(node: Node) -> Node:
    node: Node = node

    if node.val == 0:
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
        return node

def printFactorTree(root: Node) -> None:
    print(root.val)
    if (root.right != None):
        print("| \\")
        currNode: Node = root
        indentation = 0
        while True:
            valLen: int = len(str(currNode.right.val))
            if valLen == 1:
                print(" " * indentation + str(currNode.left.val) + "  " + str(currNode.right.val))
                indentation += 3
            else:
                print(" " * indentation + str(currNode.left.val) + " " + str(currNode.right.val))
                indentation += 2
            currNode = currNode.right
            if (currNode.right == None):
                break
            print(" " * indentation + "| \\")

if __name__ == '__main__':
    while True:
        try:
            i: str = input("Enter integer: ")
        except EOFError:
            print("EOF")
            exit(0)
        if(i != "exit"):
            isInt: bool = True
            try:
                num: int = int(i)
            except ValueError:
                isInt = False
            if isInt:
                root: Node = generateFactorTree(Node(num, 0))
                printFactorTree(root)
            else:
                print("Input must be an integer")
        else:
            break