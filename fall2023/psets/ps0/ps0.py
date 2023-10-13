#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

"""
###############################################
Let's build an example BinaryTree so we have 
something more concrete to chew on.

# Instantiate the nodes 
A = BTvertex('A')
B = BTvertex('B')
C = BTvertex('C')
D = BTvertex('D')

# Show who is who's child
A.left = B
A.right = C
C.right = D

# Show who is who's parent
B.parent = A
C.parent = A
D.parent = C

# Establish A as the root
tree = BinaryTree(A)


Notice how we continue building and establish
connections with other roots, like C rather than the
original root A. """


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n) 


def calculate_sizes(v):
    
    # Test if it's a base case, or null node.
    if v is None:
        return 0
    
    # Update date the size attribute for this vertex using recursion.
    left = calculate_sizes(v.left)
    right = calculate_sizes(v.right)
    v.size = left + right + 1

    return v.size
    
    

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 
    # calculate n / 2 for the initial tree
    max = r.size / 2

    # recursive helper function
    def helper(v, max):
        if v.right and v.right.size > max:
            return helper(v.right, max)
        elif v.left and v.left.size > max:
            return helper(v.left, max)
        else:
            return v

    return helper(r, max)
        