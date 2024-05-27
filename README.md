# Staff Management API

This project is a simple Flask-based API for managing staff records in a MySQL database. The API allows for the creation, retrieval, updating, and deletion of staff records.

## Features

- Retrieve all staff records
- Retrieve a specific staff record by ID
- Add a new staff record
- Update an existing staff record
- Delete a staff record
- Fetch staff job titles and related information

## Requirements

- Python 3.6+
- Flask
- Flask-MySQLdb
- MySQL database

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the MySQL database:**

    Ensure you have a MySQL server running and create a database named `mydb`. Update the Flask application configuration with your MySQL credentials.

    ```python
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "1234"
    app.config["MYSQL_DB"] = "mydb"
    app.config["MYSQL_CURSORCLASS"] = "DictCursor"
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    flask run
    ```

2. **API Endpoints:**

    - **GET /**

      Returns a simple greeting message.

      ```plaintext
      GET /
      ```

      Response:
      ```html
      <p>Hello, World!</p>
      ```

    - **GET /staff**

      Retrieves all staff records.

      ```plaintext
      GET /staff
      ```

      Response:
      ```json
      [
        {
          "staff_id": 1,
          "first_name": "John",
          "last_name": "Doe",
          ...
        },
        ...
      ]
      ```

    - **GET /staff/<id>**

      Retrieves a specific staff record by ID.

      ```plaintext
      GET /staff/1
      ```

      Response:
      ```json
      {
        "staff_id": 1,
        "first_name": "John",
        "last_name": "Doe",
        ...
      }
      ```

    - **GET /staff/<id>/job_title**

      Retrieves job title and related information for a specific staff member by ID.

      ```plaintext
      GET /staff/1/job_title
      ```

      Response:
      ```json
      {
        "staff_id": 1,
        "count": 1,
        "job_title": [
          {
            "first_name": "John",
            "contact_details": "...",
            "job_title": "Manager",
            "amount_allocated": 1000
          }
        ]
      }
      ```

    - **POST /staff**

      Adds a new staff record.

      ```plaintext
      POST /staff
      ```

      Request Body:
      ```json
      {
        "first_name": "Jane",
        "last_name": "Doe"
      }
      ```

      Response:
      ```json
      {
        "message": "staff added successfully",
        "rows_affected": 1
      }
      ```

    - **PUT /staff/<id>**

      Updates an existing staff record by ID.

      ```plaintext
      PUT /staff/1
      ```

      Request Body:
      ```json
      {
        "first_name": "Jane",
        "last_name": "Smith"
      }
      ```

      Response:
      ```json
      {
        "message": "staff updated successfully",
        "rows_affected": 1
      }
      ```

    - **DELETE /staff/<id>**

      Deletes a staff record by ID.

      ```plaintext
      DELETE /staff/1
      ```

      Response:
      ```json
      {
        "message": "staff deleted successfully",
        "rows_affected": 1
      }
      ```

    - **GET /staff/format**

      Fetches query parameters.

      ```plaintext
      GET /staff/format?id=1234&aaaa=test
      ```

      Response:
      ```json
      {
        "format": "1234",
        "foo": "test"
      }
      ```

## Notes

- Ensure the MySQL server is running and the database `mydb` is created.
- Adjust the configuration settings in the Flask app according to your MySQL server setup.
