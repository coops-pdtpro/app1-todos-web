import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if len(todos) >= 12:
        st.error("You can only have up to 12 items in your list")
    elif len(todo) > 80:
        st.error("Todo item cannot exceed 80 characters")
    elif todo in todos:
        st.error("This item is already in your list")
    else:
        todos.append(todo + "\n")
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("Coops Todo App")
st.subheader("Simple todo app to help with your tasks")
st.write("This app is to increase your productivity, simply type in a new todo item and hit enter, "
         "once completed check the tickbox to remove it from your list.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()

st.text_input(label="New Todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo", label_visibility="hidden")