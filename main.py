from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, drop_tables

from routers import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    print("App is starting up, creating tables...")
    yield
    print("App is shutting down, cleaning up resources...")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)



