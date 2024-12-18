"""
This script is used to run the FastAPI application using Uvicorn.
"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os
import sys
app = FastAPI()

# Define your FastAPI routes and endpoints here

from PIZZA.main import project_data
@app.get("/")
async def root():
    return project_data

@app.get("/order")
async def order_page():
    return HTMLResponse(content="This is the Order page.")

if __name__ == "__main__":
    uvicorn.run("manage:app", host="127.0.0.1", port=8000, reload=True)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PizzaApp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()