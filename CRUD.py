from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

users = {"1": "Имя: Example, Возраст: 18"}

@app.get("/users")
async  def users_get() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def users_post(username: str, age: int) -> str:
    user_id = str(int(max(users, key= int)) +1)
    users[user_id] = f"Имя {username}, Возраст {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def users_put(user_id: int, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"The user {user_id} is registered"

@app.delete('/user/{user_id}')
async def users_delete(user_id: int) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"

if __name__ == '__main__':
    uvicorn.run(app="CRUD:app", reload=True)