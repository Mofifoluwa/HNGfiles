from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_info():
    response_data = {
        "email": "bobbyadeniyi345@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/Mofifoluwa/HNGfiles"
    }
    # Pretty-print the JSON response
    return JSONResponse(content=json.loads(json.dumps(response_data, indent=4)))
