# 노드 클래스 정의
class TreeNode:
    def __init__(self, value, name=None):
        self.value = value
        self.left = None
        self.right = None
        self.name = None

# 트리 생성 예제
root = TreeNode(1)

a = TreeNode(2)
b = TreeNode(3, "Hi")


root.left = a
root.right = b



root.left.left = TreeNode(4)
root.left.right = TreeNode(5)



x = TreeNode(7)

root.right.right = x


y = TreeNode(6)

x.left = y


print(root.right.right.value)



# 트리 구조 출력
print(root.value)           # 1
print(root.left.value)      # 2
print(root.right.value)     # 3
print(root.left.left.value) # 4
print(root.left.right.value) # 5




# root: 1

#        1
#    2         3
#  4   5          7
#               6





#preorder, inorder, postorder traversal

def preorder_traversal(node):
    if node:
        print(node.value, end=" ")  # Root
        preorder_traversal(node.left)  # Left
        preorder_traversal(node.right)  # Right

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)  # Left
        print(node.value, end=" ")  # Root
        inorder_traversal(node.right)  # Right

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)  # Left
        postorder_traversal(node.right)  # Right
        print(node.value, end=" ")  # Root

# print("Preorder:", end=" ")
# preorder_traversal(root)  # 1 2 4 5 3

# print("\nInorder:", end=" ")
# inorder_traversal(root)   # 4 2 5 1 3

# print("\nPostorder:", end=" ")
# postorder_traversal(root) # 4 5 2 3 1



# ## BFS
# from collections import deque

# def level_order_traversal(root):
#     if not root:
#         return

#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         print(node.value, end=" ")

#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

# print("\nLevel Order:", end=" ")
# level_order_traversal(root)  # 1 2 3 4 5

# ##DFS
# def dfs(node):
#     if not node:
#         return
#     print(node.value, end=" ")
#     dfs(node.left)
#     dfs(node.right)

# print("\nDFS:", end=" ")
# dfs(root)  # 1 2 4 5 3






# class BST:
#     def __init__(self, value):
#         self.root = TreeNode(value)

#     def insert(self, value):
#         def _insert(node, value):
#             if not node:
#                 return TreeNode(value)
#             if value < node.value:
#                 node.left = _insert(node.left, value)
#             else:
#                 node.right = _insert(node.right, value)
#             return node
        
#         self.root = _insert(self.root, value)

#     def search(self, value):
#         def _search(node, value):
#             if not node or node.value == value:
#                 return node
#             if value < node.value:
#                 return _search(node.left, value)
#             return _search(node.right, value)
        
#         return _search(self.root, value) is not None

# # BST 실행 예제
# bst = BST(10)
# bst.insert(5)
# bst.insert(15)
# bst.insert(2)
# bst.insert(7)

# print(bst.search(7))  # True
# print(bst.search(20)) # False



