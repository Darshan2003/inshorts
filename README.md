### Commands to run

- `python -m pip install -r requirements.txt`
- `alembic init alembic`
- `alembic revision --autogenerate -m "New Migration"`
- `alembic upgrade head`
- `uvicorn main:app --reload`

## Update database link in main.py

## add this line in alembic/env.py
```
DATABASE_URI = 'postgresql://postgres:postgres@localhost/inshorts'
config.set_main_option('sqlalchemy.url', DATABASE_URI)

from database import models
target_metadata = models.Base.metadata
```
