def get_todos(filepath='list.txt'):
    """ Read a text file and return the lsit of to-do items 
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath='list.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#Code is only ran when it itself is ran not when another file calls upon it
if __name__ == "__main__":
    print("Hello")