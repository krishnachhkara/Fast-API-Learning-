🚀 FastAPI Learning Journey (freeCodeCamp → GenAI Roadmap)

This repository documents my step-by-step learning of FastAPI following the freeCodeCamp tutorial, aligned with a GenAI / Backend Engineer roadmap.

The goal is not just to finish a tutorial, but to build strong backend fundamentals required for:

AI / GenAI applications

Production-ready APIs

Scalable systems

SaaS & startup-oriented development

📌 Why This Repository Exists

Most tutorials focus on what to type, not why it works.

This repository focuses on:

Understanding FastAPI fundamentals deeply

Learning PostgreSQL properly (not just ORM magic)

Building APIs the industry-correct way

Preparing a strong base for GenAI systems (RAG, agents, tools)

🧭 Learning Roadmap (GenAI-Aligned)
Phase 1: Python & API Foundations

Python basics for backend

HTTP fundamentals (GET, POST, PUT, DELETE)

REST principles

JSON & request/response lifecycle

Phase 2: FastAPI Core (Current Phase)

FastAPI basics

Path & query parameters

Request body validation (Pydantic)

Status codes & HTTPException

Dependency injection

Error handling

Project structure

✔ Followed via freeCodeCamp FastAPI tutorial

Phase 3: PostgreSQL & Databases

PostgreSQL installation (Linux)

CLI (psql) usage

pgAdmin usage (GUI)

Tables, schemas, constraints

SERIAL vs IDENTITY

Sequences & auto-increment behavior

Why IDs skip values (real DB behavior)

Phase 4: FastAPI + PostgreSQL Integration

Raw SQL using psycopg

Connections, cursors

Transactions & commits

Handling DB errors properly

Mapping SQL results to JSON

⚠️ ORM (SQLAlchemy) will be introduced later, not skipped.

Phase 5: SQLAlchemy & ORM (Later)

SQLAlchemy Core & ORM

Models & relationships

Session management

Migrations (Alembic)

Avoiding common ORM traps

Phase 6: GenAI-Ready Backend

APIs for AI applications

Embeddings storage

Vector DB concepts

RAG-style backend APIs

Secure & scalable API design

🗂️ Project Structure (Evolving)
.
├── main.py            # FastAPI entry point
├── db.py              # Database connection (psycopg)
├── models/            # Future ORM models
├── schemas/           # Pydantic schemas
├── README.md          # This file
└── notes/             # Learning notes & explanations


Structure will evolve as the roadmap progresses.

🧠 Key Concepts Emphasized

Understanding over memorization

Why things break, not just how to fix them

Linux-first development (production mindset)

Clear separation of:

API layer

Database layer

Business logic

⚠️ Important Learning Principles Followed

IDs are identifiers, not row numbers

Databases allow gaps in auto-generated IDs

Lowercase table/column names (no quotes)

Raw SQL first → ORM later

Errors are part of learning, not failures

🧪 How to Run (Local)
# Install dependencies
pip install fastapi uvicorn psycopg2-binary

# Run server
uvicorn main:app --reload


PostgreSQL must be running locally.

📚 Reference

freeCodeCamp FastAPI Tutorial

PostgreSQL Official Documentation

FastAPI Official Documentation

🎯 End Goal

By the end of this roadmap, this repository will represent:

A solid FastAPI backend

A PostgreSQL-backed API

A foundation ready for GenAI applications

A codebase I fully understand — not copied blindly

🧩 Status

🟢 Active Learning
🟡 Refactoring as knowledge improves
🔵 ORM & GenAI integration coming next
