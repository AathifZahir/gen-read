# main.py
from models import Task
from fastapi import FastAPI



app = FastAPI()

todolist=[]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/tasks/")
async def create_task(task: Task):
    if len(todolist) > 0:
        last = todolist[-1]
        task.id = last.id + 1
    todolist.append(task)
    return task

@app.get("/tasks/")
async def get_tasks():
    return todolist

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for todo in todolist:
        if task_id == todo.id:
            todolist.remove(todo)
            return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}

@app.put("/tasks/{task_id}")
async def update_status(task_id: int, task_status: bool):
    for todo in todolist:
        if task_id == todo.id:
            todo.completed = task_status
            return {"message": "Task updated"}
    return {"message": "Task not found"}