from collections import deque


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"{self.value} - {self.children}"
    

class BinaryTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child):
        if len(self.children) == 2:
            raise "parent node can only have two children"
        return self.children.append(child)

    def __repr__(self):
        return f"{self.value} - {self.children}"


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right
    

root = Node(1, Node(2, Node(4), Node(5)), Node(3))


def depth_first_search_pre_order(root):
    if root is None:
        return []
    return [root.value] + depth_first_search_pre_order(root.left) + depth_first_search_pre_order(root.right)

def depth_first_search_inorder_order(root):
    if root is None:
        return []
    return depth_first_search_pre_order(root.left) + [root.value] +  depth_first_search_pre_order(root.right)

def depth_first_search_post_order(root):
    if root is None:
        return []
    return depth_first_search_pre_order(root.left) +  depth_first_search_pre_order(root.right) + [root.value]

def breadth_first_search(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def iterative_depth_first_search(root):
    if root is None:
        return []
    
    result = []
    stack = deque([root])

    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result


