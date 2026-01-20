# 🚀 FastAPI Learning Journey (freeCodeCamp → GenAI Roadmap)

This repository documents my **step-by-step learning of FastAPI** following the **freeCodeCamp tutorial**, aligned with a **GenAI / Backend Engineer roadmap**.

The goal is **not just to finish a tutorial**, but to **build strong backend fundamentals** required for:
- AI / GenAI applications
- Production-ready APIs
- Scalable systems
- SaaS & startup-oriented development

---

## 📌 Why This Repository Exists

Most tutorials focus on *what to type*, not *why it works*.

This repository focuses on:
- Understanding FastAPI fundamentals deeply
- Learning PostgreSQL properly (not just ORM magic)
- Building APIs the **industry-correct way**
- Preparing a strong base for **GenAI systems** (RAG, agents, tools)

---

## 🧭 Learning Roadmap (GenAI-Aligned)

### Phase 1: Python & API Foundations
- Python basics for backend
- HTTP fundamentals (GET, POST, PUT, DELETE)
- REST principles
- JSON & request/response lifecycle

---

### Phase 2: FastAPI Core (Current Phase)
- FastAPI basics
- Path & query parameters
- Request body validation (Pydantic)
- Status codes & HTTPException
- Dependency injection
- Error handling
- Project structure

✔ Followed via **freeCodeCamp FastAPI tutorial**

---

### Phase 3: PostgreSQL & Databases
- PostgreSQL installation (Linux)
- CLI (`psql`) usage
- pgAdmin usage (GUI)
- Tables, schemas, constraints
- `SERIAL` vs `IDENTITY`
- Sequences & auto-increment behavior
- Why IDs skip values (real DB behavior)

---

### Phase 4: FastAPI + PostgreSQL Integration
- Raw SQL using `psycopg`
- Connections, cursors
- Transactions & commits
- Handling DB errors properly
- Mapping SQL results to JSON

⚠️ ORM (SQLAlchemy) will be introduced **later**, not skipped.

---

### Phase 5: SQLAlchemy & ORM (Later)
- SQLAlchemy Core & ORM
- Models & relationships
- Session management
- Migrations (Alembic)
- Avoiding common ORM traps

---

### Phase 6: GenAI-Ready Backend
- APIs for AI applications
- Embeddings storage
- Vector DB concepts
- RAG-style backend APIs
- Secure & scalable API design

---

## 🗂️ Project Structure (Evolving)

```text
.
├── main.py            # FastAPI entry point
├── db.py              # Database connection (psycopg)
├── models/            # Future ORM models
├── schemas/           # Pydantic schemas
├── README.md          # This file
└── notes/             # Learning notes & explanations
