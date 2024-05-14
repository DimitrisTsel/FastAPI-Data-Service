# FastAPI Data Service

The FastAPI Data Service is a RESTful API built using FastAPI with Python 3.7+.
The purpose of FastAPI Data Service is designed to provide a RESTful API for handling data related to retail transactions. The API allows users to retrieve, create, and delete records of retail transactions, providing access to valuable data for analysis and application development.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
```
2. Install the dependencies:

```bash
pip install -r requirements.txt
```
## Usage
# Run locally
1. Run the FastAPI server:
```bash
uvicorn main:app --reload
```
2. Access the API endpoints in your browser or use tools like
cURL or Postman to interact with the API.

# Running as a Docker Container
1. Build the Docker image:
```bash
docker build -t fastapi-data-service .
```
2. Run the Docker container:
```bash
docker run -d -p 8000:80 fastapi-data-service
```
3. Access the API endpoints at http://localhost:8000 in your browser or through API testing tools.

## API Endpoints

GET /v1/api_status: Check the status of the API.
GET /v1/countries: Retrieve all countries.
GET /v1/countries/{country}: Retrieve data for a specific country.
POST /records: Create new records.
DELETE /v1/countries/{country}: Delete data for a specific country.
