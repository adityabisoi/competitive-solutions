def function(root):
    if root in None:
        return
    else:
        return max(1+function(root.right), 1+function(root.left))
