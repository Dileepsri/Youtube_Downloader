

from fastapi import FastAPI,  Form
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# Configure CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
import os
import yt_dlp

cur_dir = os.getcwd()




@app.post("/download")


def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir, "ABCsample.mp4")    
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status": "Download Started"}
        
        
        
        
# from fastapi import FastAPI, Form
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # CORS configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow requests from any origin
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods
#     allow_headers=["*"],  # Allow all headers
# )
# import os
# import yt_dlp
# cur_dir = os.getcwd()

# @app.post("/download")
# async def download_video(link: str = Form(...)):
#     # Your logic to handle the download
#     return {"message": "Download started", "link": link}       
