
# Library CRUD Application

This project is a simple library CRUD (Create, Read, Update, Delete) application built with a Vue.js frontend and a Django backend. The frontend communicates with the backend API using Axios for HTTP requests. The backend is built using Django and Django REST framework to serve data to the frontend.

## Table of Contents
- [Frontend](#frontend)
- [Backend](#backend)
- [Installation](#installation)
  - [Frontend](#frontend-installation)
  - [Backend](#backend-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies](#technologies)

## Frontend

The frontend is built with Vue.js, Axios, and Bun. Vue.js is used for building the user interface, while Axios is used to make HTTP requests to the backend. Bun is used as the JavaScript bundler to optimize the development process.

### Features
- Add a new book to the library
- List all books in the library
- Delete a book from the library

### Frontend Technologies
- **Vue.js**: A progressive JavaScript framework used to build the user interface.
- **Axios**: A promise-based HTTP client used to interact with the Django backend.
- **Bun**: A fast JavaScript bundler, package manager, and runtime for the frontend.

### Frontend Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-crud.git
   cd library-crud
   ```

2. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

3. Install the dependencies using Bun:
   ```bash
   bun install
   ```

4. Run the development server:
   ```bash
   bun dev
   ```

Your frontend will be available at `http://localhost:5173`.

## Backend

The backend is built with Django and the Django REST framework to provide API endpoints for the frontend.

### Features
- CRUD operations for books
- Uses the Django ORM to interact with the database
- Provides API endpoints to the frontend for book management

### Backend Technologies
- **Django**: A high-level Python web framework for rapid development.
- **Django REST Framework (DRF)**: A toolkit for building APIs with Django.

### Backend Installation

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

The backend will be available at `http://localhost:8000`.

## Usage

1. Ensure that both the frontend and backend servers are running.
2. Open the frontend in your browser at `http://localhost:5173`.
3. Use the form to add new books, view the list of books, or delete books from the library.

## API Endpoints

### `/api/books/` [GET]
- **Method**: `GET`
- **Description**: Fetches the list of books in the library.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "title": "Book Title",
      "author": "Author Name",
      "published_date": "2023-01-01",
      "isbn": "1234567890123",
      "pages": 250,
      "cover": "/media/covers/book_cover.jpg"
    },
    ...
  ]
  ```

### `/api/books/` [POST]
- **Method**: `POST`
- **Description**: Adds a new book to the library.
- **Body**:
  ```json
  {
    "title": "New Book Title",
    "author": "New Author",
    "published_date": "2025-01-01",
    "isbn": "9876543210987",
    "pages": 300
  }
  ```

### `/api/books/{id}/` [DELETE]
- **Method**: `DELETE`
- **Description**: Deletes a book by its ID.

## Technologies

- **Frontend**:
  - Vue.js
  - Axios
  - Bun

- **Backend**:
  - Django
  - Django REST Framework

- **Database**:
  - SQLite (default) or any other database configured in `settings.py`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
