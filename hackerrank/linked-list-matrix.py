def function(matrix, i, j, m, n):
    if i > m-1 and j > n-1:
        return None
    else:
        # Head with properties: right and down
        node = Node(matrix[i][j])
        node.right = function(matrix, i, j+1, m, n)
        node.down = function(matrix, i+1, j, m, n)
        return node


function(matrix, 0, 0, 4, 4)
