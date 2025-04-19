from binarytree import bst

random_bst = bst(height=5, is_perfect=True)

print(random_bst)


def find_max(root: bst):
    if not root.right:
        return root.value

    return find_max(root.right)


def find_min(root: bst):
    if not root.left:
        return root.value

    return find_min(root.left)


def sum_bst(root: bst):
    left_sum = sum_bst(root.left) if root.left else 0
    right_sum = sum_bst(root.right) if root.right else 0

    return root.value + left_sum + right_sum

min_bst = find_min(random_bst)
max_bst = find_max(random_bst)
sum_all_nodes = sum_bst(random_bst)

print(f'Min: {min_bst}')
print(f'Max: {max_bst}')
print(f'Sum: {sum_all_nodes}')