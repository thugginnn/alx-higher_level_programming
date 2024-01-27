# Python - Network #1

## Tasks

### 0. What's my status? #0

- **File**: `0-hbtn_status.py`
- **Description**: Python script that fetches [https://intranet.hbtn.io/status](https://intranet.hbtn.io/status).
- **Library**: Uses `urllib`.

### 1. Response header value #0

- **File**: `1-hbtn_header.py`
- **Description**: Python script that displays the `X-Request-Id` response header variable of a request to a given URL.
- **Usage**: `./1-hbtn_header.py <URL>`
- **Library**: Uses `urllib`.

### 2. POST an email #0

- **File**: `2-post_email.py`
- **Description**: Python script that sends a POST request to a given URL with a given email and displays the response body.
- **Usage**: `./2-post_email.py <URL> <email>`
- **Library**: Uses `urllib`.

### 3. Error code #0

- **File**: `3-error_code.py`
- **Description**: Python script sends a request to a given URL and displays the response body. Handles HTTP errors.
- **Library**: Uses `urllib`.

### 4. What's my status? #1

- **File**: `4-hbtn_status.py`
- **Description**: Python script that fetches [https://intranet.hbtn.io/status](https://intranet.hbtn.io/status).
- **Library**: Uses `requests`.

### 5. Response header value #1

- **File**: `5-hbtn_header.py`
- **Description**: Python script that displays the `X-Request-Id` response header variable of a request to a given URL.
- **Usage**: `./5-hbtn_header.py <URL>`
- **Library**: Uses `requests`.

### 6. POST an email #1

- **File**: `6-post_email.py`
- **Description**: Python script that sends a POST request to a given URL with a given email and displays the response body.
- **Usage**: `./6-post_email.py <URL> <email>`
- **Library**: Uses `requests`.

### 7. Error code #1

- **File**: `7-error_code.py`
- **Description**: Python script sends a request to a given URL and displays the response body. Handles HTTP errors.
- **Library**: Uses `requests`.

### 8. Search API

- **File**: `8-json_api.py`
- **Description**: Python script that sends a POST request to [http://0.0.0.0:5000/search_user](http://0.0.0.0:5000/search_user) with a letter passed as a parameter.
- **Usage**: `./8-json_api.py <letter>`
- **Letter Parameter**: The letter is sent as the value of the variable `q`.
- **If No Letter Given**: Sets `q=""`.
- **Response Handling**: If the response body is properly formatted and non-empty, displays it as `[<id>] <name>`.
- **Library**: Uses `requests`.

### 9. My Github!

- **File**: `10-my_github.py`
- **Description**: Python script that takes GitHub credentials (username and password) and uses the Github API to display the corresponding ID.
- **Usage**: `./10-my_github.py <username> <password>`
- **Library**: Uses `requests`.

### 10. Time for an interview!

- **File**: `100-github_commits.py`
- **Description**: Python script that lists the 10 most recent comments of a given GitHub repository using the GitHub API.
- **Usage**: `./100-github_commits.py <repository name> <owner name>`
- **Library**: Uses `requests`.
