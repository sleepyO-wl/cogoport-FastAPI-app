
# Configuration Management System

This is a robust and scalable FastAPI application for managing the configuration of onboarding requirements for organizations from different countries. The API provides functionalities for CRUD (Create, Read, Update, Delete) operations for managing configurations.

## Features

- Create configuration for a country's onboarding requirements.
- Retrieve configuration for a specific country.
- Update configuration for a specific country.
- Delete configuration for a specific country.

## Technologies Used

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

## Requirements

- Python 3.7+
- PostgreSQL

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd config_mgmt
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

- Install PostgreSQL from [PostgreSQL Downloads](https://www.postgresql.org/download/).
- Create a database named `config_mgmt`.

### 5. Configure Environment Variables

In the `.env` file in the root directory with the following content (replace `your_password` with your PostgreSQL password):

```env
DATABASE_URL=postgresql://postgres:your_password@localhost/config_mgmt
```

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Create Configuration

- **URL:** `/configurations/create_configuration`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "country_code": "IN",
    "requirements": "Business Name, PAN, GSTIN"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "country_code": "IN",
    "requirements": "Business Name, PAN, GSTIN"
  }
  ```

### Get Configuration

- **URL:** `/configurations/get_configuration/{country_code}`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "id": 1,
    "country_code": "IN",
    "requirements": "Business Name, PAN, GSTIN"
  }
  ```

### Update Configuration

- **URL:** `/configurations/update_configuration`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "country_code": "IN",
    "requirements": "Business Name, PAN, GSTIN, New Requirement"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "country_code": "IN",
    "requirements": "Business Name, PAN, GSTIN, New Requirement"
  }
  ```

### Delete Configuration

- **URL:** `/configurations/delete_configuration`
- **Method:** `DELETE`
- **Request Body:**
  ```json
  {
    "country_code": "IN"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "country_code": "IN",
    "requirements": "Business Name, PAN, GSTIN, New Requirement"
  }
  ```
