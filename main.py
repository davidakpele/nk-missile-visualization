from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI(
    title="North Korea Missile Test Visualization",
    description="An interactive visualization of flight tests of all missiles launched by North Korea from 1984 to 2025",
    version="1.0.0"
)

# Mount all static directories
app.mount("/css", StaticFiles(directory="static/css"), name="css")
app.mount("/js", StaticFiles(directory="static/js"), name="js")
app.mount("/images", StaticFiles(directory="static/images"), name="images")
app.mount("/data", StaticFiles(directory="static/data"), name="data")

@app.get("/")
async def read_root():
    # Read and return the HTML file
    with open("static/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)