from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home(): 
    return {
        "status": "200",
        "message": "App working. on home page"
    }
# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"user_id": user_id, "full_name": "Danny Manny", "email": "danny.manny@gmail.com"}

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
    print("server running")