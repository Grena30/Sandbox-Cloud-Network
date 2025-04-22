#!/bin/bash

# Register the service with Consul
python register.py

# Start the FastAPI app
exec uvicorn main:app --host 0.0.0.0 --port 8000