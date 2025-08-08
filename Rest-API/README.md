# REST API with Flask

A complete REST API built with Flask for managing user data with full CRUD operations, persistent storage, and comprehensive error handling. Features a clean API design following REST principles with JSON responses and proper HTTP status codes.

## 📋 Project Overview

This is a Python Flask-based REST API that provides complete user management functionality. The API supports all standard CRUD operations (Create, Read, Update, Delete) with persistent file storage, input validation, and proper HTTP status codes. It's designed following REST architectural principles and includes colored terminal logging for development monitoring.

## ✨ Features

### API Endpoints
- **GET /users** - Retrieve all users
- **GET /users/{id}** - Retrieve a specific user by ID
- **POST /users** - Create a new user
- **PUT /users/{id}** - Update an existing user
- **DELETE /users/{id}** - Delete a user

### Core Functionality
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Persistent Storage**: Users are saved to and loaded from a text file
- **Auto-incrementing IDs**: Automatic unique ID generation
- **Input Validation**: Comprehensive request validation
- **Error Handling**: Proper HTTP status codes and error messages
- **JSON Responses**: All responses in JSON format

### Advanced Features
- **File-based Persistence**: Automatic data persistence between server restarts
- **Colored Logging**: Development-friendly colored console output
- **Data Integrity**: Automatic file and directory creation
- **UTF-8 Support**: International character support
- **RESTful Design**: Follows REST architectural principles

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Required Python packages:
  - `Flask` - Web framework
  - `colorama` - Colored terminal output

### Installation

1. Clone or download the repository:
   ```bash
   git clone <repository-url>
   cd Rest-API
   ```

2. Install required dependencies:
   ```bash
   pip install Flask colorama
   ```

   Or create a requirements.txt file:
   ```txt
   Flask==2.3.3
   colorama==0.4.6
   ```

   Then install:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Navigate to the Rest-API directory and run:

```bash
python flask_app.py
```

The API will be available at: `http://127.0.0.1:5000`

## 📖 API Documentation

### Base URL
```
http://127.0.0.1:5000
```

### Endpoints

#### 1. Get All Users
- **URL**: `/users`
- **Method**: `GET`
- **Description**: Retrieve all users
- **Response**: Array of user objects

**Example Request:**
```bash
curl -X GET http://127.0.0.1:5000/users
```

**Example Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com"
  }
]
```

#### 2. Get User by ID
- **URL**: `/users/{id}`
- **Method**: `GET`
- **Description**: Retrieve a specific user by ID
- **Parameters**: `id` (integer) - User ID
- **Response**: User object or 404 if not found

**Example Request:**
```bash
curl -X GET http://127.0.0.1:5000/users/1
```

**Example Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

#### 3. Create New User
- **URL**: `/users`
- **Method**: `POST`
- **Description**: Create a new user
- **Content-Type**: `application/json`
- **Required Fields**: `name`
- **Optional Fields**: `email`

**Example Request:**
```bash
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

**Example Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

#### 4. Update User
- **URL**: `/users/{id}`
- **Method**: `PUT`
- **Description**: Update an existing user
- **Parameters**: `id` (integer) - User ID
- **Content-Type**: `application/json`
- **Optional Fields**: `name`, `email`

**Example Request:**
```bash
curl -X PUT http://127.0.0.1:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}'
```

**Example Response:**
```json
{
  "id": 1,
  "name": "John Updated",
  "email": "john.updated@example.com"
}
```

#### 5. Delete User
- **URL**: `/users/{id}`
- **Method**: `DELETE`
- **Description**: Delete a user
- **Parameters**: `id` (integer) - User ID
- **Response**: Success confirmation or 404 if not found

**Example Request:**
```bash
curl -X DELETE http://127.0.0.1:5000/users/1
```

**Example Response:**
```json
{
  "result": true
}
```

### HTTP Status Codes

- **200 OK** - Successful GET, PUT, DELETE
- **201 Created** - Successful POST (user created)
- **400 Bad Request** - Invalid input data
- **404 Not Found** - User not found
- **500 Internal Server Error** - Server error

### Error Responses

```json
{
  "error": "User not found"
}
```

```json
{
  "error": "Invalid input: 'name' is required"
}
```

## 🏗️ Code Architecture

### Application Structure

```
Rest-API/
├── flask_app.py        # Main application file
├── users.txt          # Data storage file (auto-created)
├── requirements.txt    # Dependencies (optional)
└── README.md          # This documentation
```

### Key Components

#### Flask Application Setup
```python
from flask import Flask, jsonify, request, abort
app = Flask(__name__)
```

#### Data Storage
- **File-based Storage**: Users stored in `users.txt`
- **Format**: `id||name||email` per line
- **In-memory Cache**: Dictionary for fast access

#### Core Functions

##### `load_users()`
- Loads user data from file into memory
- Creates file/directory if they don't exist
- Parses delimited format into dictionary

##### `save_users()`
- Persists current user data to file
- UTF-8 encoding for international characters
- Atomic write operation

##### `get_next_id()`
- Generates unique auto-incrementing IDs
- Handles empty database case
- Ensures no ID conflicts

### Data Model

```python
user = {
    "id": int,      # Auto-generated unique identifier
    "name": str,    # Required field, user's name
    "email": str    # Optional field, user's email
}
```

## 💾 Data Persistence

### File Format
Users are stored in `Rest-API/users.txt` with the following format:
```
1||John Doe||john@example.com
2||Jane Smith||jane@example.com
3||Bob Wilson||bob@example.com
```

### Storage Features
- **Automatic Creation**: File and directory created automatically
- **UTF-8 Encoding**: Support for international characters
- **Delimiter-based**: Uses `||` as field separator
- **Human Readable**: Plain text format for easy debugging

## 🛡️ Error Handling

### Input Validation
- **Required Fields**: Name field is mandatory
- **Empty Values**: Prevents empty name creation
- **JSON Format**: Validates JSON request format
- **Data Types**: Ensures proper data types

### HTTP Error Responses
- **400 Bad Request**: Invalid input data
- **404 Not Found**: User doesn't exist
- **500 Internal Server Error**: Server-side errors

### Server-side Logging
- 🟢 Green: User creation events
- 🔵 Blue: User update events
- 🔴 Red: User deletion events
- 🔵 Cyan: Server startup message

## 🔧 Testing the API

### Using curl

```bash
# Get all users
curl -X GET http://127.0.0.1:5000/users

# Get specific user
curl -X GET http://127.0.0.1:5000/users/1

# Create user
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Test User", "email": "test@example.com"}'

# Update user
curl -X PUT http://127.0.0.1:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name"}'

# Delete user
curl -X DELETE http://127.0.0.1:5000/users/1
```

### Using Postman

1. **Import Collection**: Create a new collection in Postman
2. **Set Base URL**: `http://127.0.0.1:5000`
3. **Add Requests**: Create requests for each endpoint
4. **Set Headers**: Add `Content-Type: application/json` for POST/PUT
5. **Test Scenarios**: Test valid and invalid inputs

### Using Python requests

```python
import requests
import json

base_url = "http://127.0.0.1:5000"

# Get all users
response = requests.get(f"{base_url}/users")
print(response.json())

# Create user
user_data = {"name": "Test User", "email": "test@example.com"}
response = requests.post(f"{base_url}/users", json=user_data)
print(response.json())

# Update user
update_data = {"name": "Updated Name"}
response = requests.put(f"{base_url}/users/1", json=update_data)
print(response.json())

# Delete user
response = requests.delete(f"{base_url}/users/1")
print(response.json())
```

## 🚀 Deployment

### Development Server
The application runs on Flask's development server by default:
```python
app.run(debug=True)
```

### Production Deployment
For production, consider using:
- **Gunicorn**: WSGI HTTP Server
- **uWSGI**: Alternative WSGI server
- **Docker**: Containerized deployment
- **Cloud Platforms**: Heroku, AWS, Google Cloud

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 flask_app:app
```

## 🔒 Security Considerations

### Current Implementation
- Basic input validation
- No authentication/authorization
- Development server (not production-ready)

### Production Recommendations
- **Authentication**: Implement JWT or session-based auth
- **HTTPS**: Use SSL/TLS encryption
- **Rate Limiting**: Prevent API abuse
- **Input Sanitization**: Enhanced validation
- **CORS**: Configure cross-origin requests
- **Database**: Use proper database instead of file storage

## 🚀 Future Enhancements

### Features
- **User Authentication**: Login/logout functionality
- **Data Validation**: Enhanced input validation
- **Pagination**: For large user lists
- **Search/Filter**: User search capabilities
- **User Roles**: Admin/user permissions
- **API Versioning**: Version management

### Technical Improvements
- **Database Integration**: SQLite, PostgreSQL, or MongoDB
- **ORM**: SQLAlchemy integration
- **API Documentation**: Swagger/OpenAPI
- **Unit Tests**: Comprehensive test suite
- **Logging**: Structured logging with levels
- **Configuration**: Environment-based config

### Performance
- **Caching**: Redis or in-memory caching
- **Async Support**: Async/await patterns
- **Connection Pooling**: Database optimization
- **Load Balancing**: Multiple server instances

## 📋 Best Practices

### RESTful Design
- Use appropriate HTTP methods
- Return proper status codes
- Implement consistent URL patterns
- Use JSON for data exchange

### Error Handling
- Provide meaningful error messages
- Use standard HTTP status codes
- Include error details in responses
- Log errors for debugging

### Security
- Validate all inputs
- Sanitize data before storage
- Implement authentication
- Use HTTPS in production

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Database integration
- Authentication system
- Enhanced validation
- API documentation
- Unit tests
- Performance optimizations

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as part of the Elevate Labs development exercises.

## 🐛 Troubleshooting

### Common Issues

1. **Module not found (Flask)**:
   ```bash
   pip install Flask colorama
   ```

2. **Port already in use**:
   - Change the port in the code or kill the existing process
   ```python
   app.run(debug=True, port=5001)
   ```

3. **File permission errors**:
   - Ensure write permissions in the application directory

4. **JSON parsing errors**:
   - Verify Content-Type header is set to `application/json`
   - Check JSON format validity

5. **Connection refused**:
   - Ensure the Flask server is running
   - Check if firewall is blocking the port

### Debug Mode

The application runs in debug mode by default, which provides:
- Automatic reloading on code changes
- Detailed error messages
- Interactive debugger in browser

Disable for production:
```python
app.run(debug=False)
```

---

**Note**: This REST API is designed for educational purposes and demonstrates fundamental web API development concepts. For production use, implement proper security measures and use a production-grade database.