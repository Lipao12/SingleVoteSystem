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
    "candidateId": "candidate_id",
    "voterIP": "voter_ip"
  }
  ```

- **Fields**:
  `candidateId`: The ID of the candidate for whom the vote is being recorded.
  `voterIP`: The IP address of the voter, used to ensure that the IP has not already voted.\*\*

### **Respose**:

- **Status Code**:
  200 OK - Vote successfully recorded.
  400 Bad Request - Error in recording the vote (e.g., if the candidate does not exist or the IP has already voted).

- **Response Body (JSON)**:

  ```json
  {
    "message": "Success or error message",
    "status": 200
  }
  ```

### Get All Candidates

- **Endpoint**: `/candidates`
- **HTTP Method**: `GET`
- **Description**: Retrieves a list of all candidates from the database. You can specify which columns to return.

#### Query Parameters

- **`columns`** (optional): A comma-separated list of column names to include in the response. If not provided, all columns will be returned.

#### Example Request

To retrieve specific columns (e.g., `id`, `name`, and `vote_qnt`):

#### Response

- **Status Code**:

  - `200 OK` - Successfully retrieved the candidate data.
  - `404 Not Found` - No candidates found in the database.
  - `500 Internal Server Error` - Error occurred while accessing the database.

- **Response Body**:

  If specific columns are requested:

  ```json
  {
    "columns": ["id", "name", "vote_qnt"],
    "data": [
      ["1", "Candidate 1", 10],
      ["2", "Candidate 2", 5]
    ]
  }
  ```
