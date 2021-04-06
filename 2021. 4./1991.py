########## BOJ ##########
# 1991: 트리 순회

# 전위 순회
def preorder(node):
    if node != '.':
        print('{}'.format(node), end='')
        preorder(tree[node][0])  # left
        preorder(tree[node][1])  # right


# 중위 순회
def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print('{}'.format(node), end='')
        inorder(tree[node][1])


# 후위 순회
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print('{}'.format(node), end='')



N = int(input()) # number of nodes
# tree = [[0] * 3 for _ in range(N+1)]
tree = {} # dictionary (key:value) as (parent:child)
for i in range(1, N+1):
    node, left, right = input().split()
    tree[node] = [left, right]

print(tree)

root = 'A'
preorder(root)
print()
inorder(root)
print()
postorder(root)



"""
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.
"""