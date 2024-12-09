
# Library Management System

A backend application for managing library books and users, designed with Flask and SQLAlchemy. This project implements RESTful APIs for librarians and users, JWT-based authentication, CSV download functionality, and role-based access control.

## Features

### Librarian APIs
1. **Create a new library user** (email, password, role).
2. **View all book borrow requests.**
3. **Approve or deny a borrow request.**
4. **View a user's book borrowing history.**

### Library User APIs
1. **Get a list of books** available in the library.
2. **Submit a borrow request** for a specific book.
3. **View personal book borrowing history.**
4. **Download borrowing history as a CSV file.**

### Additional Features
- JWT-based authentication for secure access.
- Role-based access control to differentiate librarian and user permissions.
- Validation for overlapping borrowing dates.
- User-friendly error handling for invalid or incomplete requests.
- Deployment-ready setup for Vercel.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Flask and dependencies
- SQLite (pre-configured for development)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Surytejaswini66/library-management-system.git
   cd library-management-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## API Endpoints

### Authentication
- **Login:**  
  `POST /auth/login`  
  **Payload:**  
  ```json
  {
    "email": "user@example.com",
    "password": "password"
  }
  ```  

### Librarian Routes
- **Create User:**  
  `POST /librarian/create-user`  
  **Headers:** `Authorization: Bearer <token>`  
  **Payload:**  
  ```json
  {
    "email": "newuser@example.com",
    "password": "password",
    "role": "user"
  }
  ```

- **View Borrow Requests:**  
  `GET /librarian/borrow-requests`  
  **Headers:** `Authorization: Bearer <token>`  

### User Routes
- **Get Books:**  
  `GET /books`  
  **Headers:** `Authorization: Bearer <token>`  

- **Borrow Book:**  
  `POST /borrow`  
  **Headers:** `Authorization: Bearer <token>`  
  **Payload:**  
  ```json
  {
    "book_id": 1,
    "from_date": "2024-12-10",
    "to_date": "2024-12-15"
  }
  ```

- **View Personal History:**  
  `GET /borrow/history`  
  **Headers:** `Authorization: Bearer <token>`  

- **Download History (CSV):**  
  `GET /borrow/download`  
  **Headers:** `Authorization: Bearer <token>`  

---

## Deployment

### Vercel Deployment
1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Configure the project:
   ```bash
   vercel init
   ```

3. Deploy the project:
   ```bash
   vercel --prod
   ```

4. Verify deployment by accessing the provided Vercel URL.

---

## Database Schema
- **Users Table:**  
  `id`, `email`, `password`, `role`

- **Books Table:**  
  `id`, `title`, `available`

- **Borrow Requests Table:**  
  `id`, `user_id`, `book_id`, `from_date`, `to_date`, `status`

---

## Testing
### Step-by-Step Testing Using Postman

1. **Run the Application Locally:**
   ```bash
   python app.py
   ```

2. **Login:**
   - **Method:** POST  
   - **Endpoint:** `http://127.0.0.1:5000/auth/login`  
   - **Body:**
     ```json
     {
       "email": "admin@example.com",
       "password": "adminpassword"
     }
     ```

3. **Test All Endpoints:**  
   Follow the API Endpoints section for details on how to test each route.

---

