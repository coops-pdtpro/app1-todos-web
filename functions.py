FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the todos from the file and return them as a list. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todos to the file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__cli__":
    print("Hello")
    print(get_todos())