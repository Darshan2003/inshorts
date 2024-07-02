### Commands to run

- `python -m pip install -r requirements.txt`
- `alembic init alembic`
- `alembic revision --autogenerate -m "New Migration"`
- `alembic upgrade head`
- `uvicorn main:app --reload`
