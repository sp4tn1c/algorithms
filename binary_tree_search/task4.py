import sys


class AvlNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0


class AVL:
    def __init__(self):
        self.root = None

    def height_node(self, node):
        return -1 if node is None else node.height

    def update(self, node):
        node.height = 1 + max(self.height_node(node.left), self.height_node(node.right))

    def balance_factor(self, node):
        return self.height_node(node.right) - self.height_node(node.left)

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self.update(y)
        self.update(x)
        return x

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self.update(x)
        self.update(y)
        return y

    def rebalance(self, node):
        self.update(node)
        bf = self.balance_factor(node)
        
        if bf > 1:
            if self.balance_factor(node.right) >= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        
        if bf < -1:
            if self.balance_factor(node.left) <= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        
        return node

    def avl_insert(self, root, key):
        if root is None:
            return AvlNode(key)
        if key == root.key:
            return root
        if key < root.key:
            root.left = self.avl_insert(root.left, key)
        else:
            root.right = self.avl_insert(root.right, key)
        return self.rebalance(root)

    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def avl_delete(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.avl_delete(root.left, key)
        elif key > root.key:
            root.right = self.avl_delete(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ = self.find_min(root.right)
            root.key = succ.key
            root.right = self.avl_delete(root.right, succ.key)
        return self.rebalance(root)

    def add(self, key):
        self.root = self.avl_insert(self.root, key)

    def delete(self, key):
        self.root = self.avl_delete(self.root, key)

    def exists(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            current = current.left if key < current.key else current.right
        return False

    def next_key(self, x):
        current = self.root
        answer = None
        while current is not None:
            if current.key >= x:
                answer = current.key
                current = current.left
            else:
                current = current.right
        return answer

    def prev_key(self, x):
        current = self.root
        answer = None
        while current is not None:
            if current.key <= x:
                answer = current.key
                current = current.right
            else:
                current = current.left
        return answer

    def root_key(self):
        return 'Empty' if self.root is None else str(self.root.key)

    def tree_height(self):
        return self.height_node(self.root) + 1

    def preorder(self):
        if self.root is None:
            return 'Empty'
        keys = []
        def traverse(node):
            if node is not None:
                keys.append(str(node.key))
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return ' '.join(keys)


def main():
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split('\n')
    q = int(input_data[0])
    tree = AVL()
    result_f = []
    for line in input_data[1:q + 1]:
        cmd = line.split()
        if not cmd:
            continue
        if cmd[0] == 'add':
            tree.add(int(cmd[1]))
        elif cmd[0] == 'del':
            tree.delete(int(cmd[1]))
        elif cmd[0] == 'exists':
            result_f.append('YES' if tree.exists(int(cmd[1])) else 'NO')
        elif cmd[0] == 'next':
            result = tree.next_key(int(cmd[1]))
            result_f.append(str(result) if result is not None else 'None')
        elif cmd[0] == 'prev':
            result = tree.prev_key(int(cmd[1]))
            result_f.append(str(result) if result is not None else 'None')
        elif cmd[0] == 'root':
            result_f.append(tree.root_key())
        elif cmd[0] == 'height':
            result_f.append(str(tree.tree_height()))
        elif cmd[0] == 'print':
            result_f.append(tree.preorder())
    print('\n'.join(result_f))


main()
