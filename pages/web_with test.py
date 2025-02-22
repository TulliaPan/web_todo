import streamlit as st
import functions
import os

todos=functions.get_todos()
st.set_page_config(layout="wide")
if not os.path.exists("todo.txt"):
    with open("todo.txt","w")as file:
        pass
def add_todo():
    todo=st.session_state["new"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.text_input(label="enter new todo",placeholder="add new todo here, or the new edited todo",
              on_change=add_todo, key="new")


st.title("To do app")
st.subheader("this is an app where you can follow your to do")
st.write("this app increse your <b>producitvity</b>,check when completed")

for i,todo in enumerate(todos):
    check=st.checkbox(todo,key=todo)
    if check:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



#st.text_input(label="edit your todo",placeholder="modify your todo here",
#              key="edit")

#def edit_todo():
#    todo_edit=st.session_state["edit"]
#    new_todo=st.session_state["new"]
#    index = todos.index(todo_edit)
#    todos[index] = new_todo
#    functions.write_todos(todos)