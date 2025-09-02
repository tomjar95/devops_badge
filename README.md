# devops_badge
## Project Overview
This is a simple FastAPI application contenerized with Docker and integrated with Github Actions for CI/CD.

## Features & Usage
The application exposes a minimal notes API:
- `GET /` -> returnes a welcome message
- `POST /notes?note=text` -> adds a new note
- `GET /notes` -> retrieves all notes (stored only in memory)

## Run locally
```
git clone https://github.com/tomjar95/devops_badge.git
cd devops_badge/
```

### Without Docker
```bash
git clone https://github.com/tomjar95/devops_badge.git
cd /app
pip install -r requirements.txt
uvicorn main:app --reload
```

### With docker
```bash
docker build -t devops_badge .
docker run -p 8000:8000 devops_badge
```

The API will be available at: http://localhost:8000
Docs: http://localhost:8000/docs


## Testing
GitHub Actions automatically run the tests and build a Docker image on every push or pull request, ensuring continuous integration.
