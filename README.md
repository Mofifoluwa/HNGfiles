# FastAPI API for HNG Backend Task

This is a simple FastAPI-based API that provides essential information, including an email, the current datetime, and a GitHub repository link. The API also supports Cross-Origin Resource Sharing (CORS).

## Features
- Returns JSON-formatted data containing email, current datetime, and GitHub repo.
- Supports CORS for cross-origin requests.
- Deployed using FastAPI and Uvicorn.

## Endpoints
### `GET /`
Returns JSON response:
```json
{
    "email": "bobbyadeniyi345@gmail.com",
    "current_datetime": "2025-02-07T14:32:01.825697+00:00",
    "github_url": "https://github.com/Mofifoluwa/HNGfiles"
}
```

## Installation & Usage
### Prerequisites
- Python 3.12+
- Git

### Clone the Repository
```bash
git clone https://github.com/Mofifoluwa/HNGfiles.git
cd HNGfiles
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the API Locally
```bash
uvicorn main:app --reload
```
The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## CORS Handling
CORS is enabled in `main.py` to allow requests from any origin:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
This ensures the API is accessible from any frontend application.

## Deployment
You can deploy the API using services like:
- **Heroku**
- **Railway.app**
- **Render**
- **AWS Lambda (with FastAPI and Mangum)**

## License
This project is open-source under the MIT License.

## Author
- **Bobby Adeniyi**  
  GitHub: [Mofifoluwa](https://github.com/Mofifoluwa)
