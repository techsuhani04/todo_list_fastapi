
# 📝 Todo List API with FastAPI (In-Memory Version)

A beginner-friendly Todo List REST API built using **FastAPI** and **Pydantic**.  
This version stores todos in-memory using Python lists (no external database required) — great for learning CRUD APIs and backend fundamentals.

---

## 🚀 Features

- Create, Read, Update, Delete (CRUD) todos
- FastAPI-powered backend
- Auto-generated Swagger UI at `/docs`
- Simple in-memory storage (data lost on restart)
- Fully written in Python

---

## 📁 Project Structure

```
todo-api-fastapi-memory/
├── main.py         # All API routes and logic
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/techsuhani04/todo_list_fastapi.git
cd todo_list_fastapi
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn pydantic
```

---

## ▶️ Run the App

```bash
uvicorn main:app --reload
```

Then open your browser and go to:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Sample Todo Format (JSON)

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

---

## 📚 API Endpoints

| Method | Endpoint         | Description          |
|--------|------------------|----------------------|
| GET    | `/`              | Welcome message      |
| POST   | `/todos`         | Create a new todo    |
| GET    | `/todos`         | Get all todos        |
| GET    | `/todos/{id}`    | Get a todo by ID     |
| PUT    | `/todos/{id}`    | Update a todo by ID  |
| DELETE | `/todos/{id}`    | Delete a todo by ID  |

---

## ✅ Author

- **Suhani Shah** – *Python & FastAPI Enthusiast*

---

## 🧠 Note

This version uses in-memory Python lists — it’s great for learning, but **not recommended for production**. If you'd like to use a persistent database, check out the SQLite version.

---

## 🌟 Give it a star if you found it helpful!
