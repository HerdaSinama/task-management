# Task Management Platform

This is a Django-based task management platform that allows users to manage their tasks
with advanced features like role-based access control, REST API, task filtering, and email notifications.

## Features
- User authentication and role-based access (Admin, User).
- Create, update, and delete tasks.
- Filter and search tasks by status, priority, or deadline.
- REST API for integration with other services (powered by Django REST Framework).
- Email notifications for task updates (powered by Celery and Redis).
- Real-time notifications using WebSocket (Django Channels).
- Optimized database queries for performance.
- Deployed and production-ready setup.

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS (Django templates)
- **Asynchronous Tasks:** Celery + Redis
- **WebSocket:** Django Channels
- **Deployment:** Gunicorn, Nginx, Docker

## Installation

### Prerequisites
- Python 3.9 or later
- PostgreSQL
- Redis
- Docker (optional for deployment)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
   ```
   
2. Set up a virtual environment:
  ```bash
  python -m venv venv
  source venv\Scripts\activate
  ```

3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Configure the .env file:
   - Create a .env file in the project root with the following variables:
  ```makefile
  SECRET_KEY=your-secret-key
  DEBUG=True
  DATABASE_URL=postgresql://username:password@localhost:5432/task_db
  REDIS_URL=redis://localhost:6379/0
  ```

5. Apply database migrations:
  ```bash
  python mamge.py migrate
  ```

6. Run the development server:
  ```bash
  python manage.py runserver 
  ```

7. Access the application at http://127.0.0.1:8000

## Usage
