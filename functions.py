def get_todos(filepath='todo.txt'):
    """read the txt file and return his content """
    with open(filepath, 'r') as file:
        user_text_local = file.readlines()
        return user_text_local


def write_todos(user_text_local):
    with open('todo.txt', 'w') as file:
        file.writelines(user_text_local)
        print("ciao")

if __name__=="__main__":
    print("Hello")
    print(get_todos())