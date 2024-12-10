import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo in todos:
        st.error("This item is already in your list")
    else:
        todos.append(todo)
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()

st.text_input(label="New Todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo", label_visibility="hidden")