class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side):
        '''
        Inserts a new doctor node under a specific parent on the given side.
        '''
        new_node = DoctorNode(doctor_name)
        parent = self._find(self.root, parent_name)
        if not parent:
            print(f"Parent '{parent_name}' not found.")
            return

        if side == "left":
            parent.left = new_node
        elif side == "right":
            parent.right = new_node
        else:
            print("Side must be 'left' or 'right'.")

    def _find(self, node, name):
        '''
        Recursively finds a node by name.
        '''
        if not node:
            return None
        if node.name == name:
            return node

        left_result = self._find(node.left, name)
        if left_result:
            return left_result
        return self._find(node.right, name)

    def preorder(self, node):
        '''
        Preorder traversal: root -> left -> right
        '''
        if not node:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        '''
        Inorder traversal: left -> root -> right
        '''
        if not node:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        '''
        Postorder traversal: left -> right -> root
        '''
        if not node:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]



# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))   # ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    print(tree.inorder(tree.root))    # ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    print(tree.postorder(tree.root))  # ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]


# A tree is appropriate for the doctor structure because it clearly shows the hierarchy between doctors and their reports. Each doctor can have two people reporting to them, which fits perfectly with the idea of parent and child nodes in a binary tree.
# It also makes it easier to organize and visualize who works under who, and to find relationships quickly by moving through the tree.
# A software engineer might use different traversals depending on what they need to do with the data.
# Preorder traversal is useful when you want to process the parent before the children, like copying or saving a tree structure. Inorder traversal is great for getting data in a sorted or logical order, especially for binary search trees.
#Postorder traversal is helpful when you need to handle or delete children before the parent, like when freeing up memory or evaluating mathematical expressions in tree form.
# Heaps are helpful for simulating real-time systems like emergency intake because they automatically keep the most urgent cases at the top. In a min-heap, the patient with the lowest urgency number
# always stays at the root, so the system can serve them first without checking every record.
#This makes it efficient to handle continuous updates as new patients arrive or old ones are removed. Overall, heaps make real-time decision-making faster and more organized, just like how emergency rooms must prioritize patients based on urgency.