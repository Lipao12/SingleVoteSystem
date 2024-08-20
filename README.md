# API Documentation

## Introduction

This API allows you to vote for candidates and retrieve information about them. The endpoints are defined to manage votes and obtain candidate information.

## Endpoints

### 1. Vote for a Candidate

- **Endpoint**: `/vote`
- **HTTP Method**: `POST`
- **Description**: Registers a vote for a specific candidate.

#### Request

- **Request Body (JSON)**:

  ```json
  {
    "candidateId": "candidate_id"
  }
  ```

- **Fields**:
  - `candidateId`: The ID of the candidate for whom the vote is being recorded.

### **Respose**:

- **Status Code**:

  - 200 OK - Vote successfully recorded.
  - 400 Bad Request - Error in recording the vote (if the candidate does not exist or the IP has already voted).

- **Response Body (JSON)**:

  ```json
  {
    "candidateId": "XXXX",
    "message": "Success message",
    "status": 200
  }
  ```

### Get All Candidates

- **Endpoint**: `/candidates`
- **HTTP Method**: `GET`
- **Description**: Retrieves a list of all candidates from the database. You can specify which columns to return.

#### Query Parameters

- **`columns`** (optional): A comma-separated list of column names to include in the response. If not provided, all columns will be returned.

#### Request

- **Request Body (JSON)**:

  ```json
  {
    "columns": ["id", "name"]
  }
  ```

To retrieve specific columns `id`, `name`, and `vote_qnt`.

#### Response

- **Status Code**:

  - `200 OK` - Successfully retrieved the candidate data.
  - `404 Not Found` - No candidates found in the database.
  - `500 Internal Server Error` - Error occurred while accessing the database.

- **Response Body**:

  If specific columns are requested:

  ```json
  {
    "data": [
      ["00001", "Candidate 1"],
      ["00002", "Candidate 2"]
    ]
  }
  ```
