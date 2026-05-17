# 📦 Basic Inventory

Basic Inventory is a small full-stack product catalog application with a **FastAPI** backend and a **React** frontend.

## ✨ Features

- 🗂️ View all products in a sortable table
- 🔎 Search products by ID, name, or description
- ➕ Add new products
- ✏️ Edit existing products
- 🗑️ Delete products
- 🔄 Refresh data from the backend

## 🧰 Tech Stack

- ⚙️ Backend: FastAPI, SQLAlchemy
- 🎨 Frontend: React, Axios
- 🗃️ Database: PostgreSQL

## 📁 Project Structure

```text
basic_inventory/
├── main.py
├── database.py
├── database_models.py
├── models.py
└── frontend/
    ├── package.json
    ├── public/
    └── src/
```

## 🚀 Getting Started

### 1) Backend

Create and activate your virtual environment if needed, then install the Python dependencies used by the backend.

Start the API server from the project root:

```bash
uvicorn main:app --reload
```

The backend is expected to run at:

```text
http://localhost:8000
```

### 2) Frontend

Install the React dependencies and start the frontend app:

```bash
cd frontend
npm install
npm start
```

The frontend runs at:

```text
http://localhost:3000
```

## 🔌 API Endpoints

- `GET /products` - list all products
- `GET /products/{id}` - get one product by ID
- `POST /products` - create a product
- `PUT /products` - update a product
- `DELETE /products/{id}` - delete a product

## 🔗 Frontend to Backend Connection

The React app calls the backend at `http://localhost:8000`.

If the frontend shows `ERR_CONNECTION_REFUSED`, it usually means the backend server is not running or is not listening on port `8000`.

## ⚠️ Notes

- The backend enables CORS for `http://localhost:3000`.
- Make sure PostgreSQL is running and the connection string in `database.py` matches your local setup.
- If you change the backend port, update the frontend API base URL in `frontend/src/App.js`.

## 🧪 Example Workflow

1. Start PostgreSQL.
2. Run the backend with `uvicorn main:app --reload`.
3. Run the frontend with `npm start` inside `frontend/`.
4. Open `http://localhost:3000` in your browser.

## 🛠️ Troubleshooting

- `ERR_CONNECTION_REFUSED`: the backend is down, crashed, or on the wrong port.
- `500 Internal Server Error` on the frontend: check the backend terminal logs for the real exception.
- Empty table or failed requests: confirm the database tables exist and the backend can connect to PostgreSQL.
