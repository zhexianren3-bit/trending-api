"""
热门话题 API
"""
from fastapi import FastAPI
app = FastAPI(title="热门话题API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "热门话题API"}

@app.get("/topics")
def topics():
    return {"success": True, "topics": [
        {"tag": "#今日话题", "posts": 1234},
        {"tag": "#热门挑战", "posts": 2345},
    ]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
