class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.
    '''
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # If the tree is empty
        if self.root is None:
            print("⚠️ No team lead found. Please add a team lead first.")
            return

        if current_node is None:
            current_node = self.root

        # If current node is the manager we're looking for
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                else:
                    print(f"⚠️ {manager_name}'s LEFT side is already occupied.")
            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                else:
                    print(f"⚠️ {manager_name}'s RIGHT side is already occupied.")
            else:
                print("❌ Invalid side. Please enter 'left' or 'right'.")
            return

        # Continue searching in the left and right subtrees
        if current_node.left:
            self.insert(manager_name, employee_name, side, current_node.left)
        if current_node.right:
            self.insert(manager_name, employee_name, side, current_node.right)

    def print_tree(self, node=None, level=0):
        if self.root is None:
            print("⚠️ The team is empty.")
            return

        if node is None and level == 0:
            node = self.root
        elif node is None:
            return

        print("  " * level + "- " + node.name)
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ").lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


"""
The recursive insert worked by starting at the root and checking each manager one at a time
until it found the right person. When the correct manager was found, the program added the new
employee to the left or right side depending on what the user picked. The recursion made it
easier to move down the tree without writing a long loop.

One problem I ran into was making sure the new employee only got added once and not in both
sides of the tree. Another challenge was handling cases where the manager didnt exist or a
side was already taken. Adding print messages helped me understand what part of the code was
running.

Trees are useful because they show relationships really clearly, like how managers and
employees are connected. They also make it easy to search or add new people without checking
every single item like in a list. This project helped me understand recursion better and how
trees can organize information in a simple way.
"""
