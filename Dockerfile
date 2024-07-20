# Phase 1: Setting up the Python/FastAPI backend
FROM python:3.11

# Set the working directory for the backend
WORKDIR /app

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files into the container
COPY . /app/

# Configure the command to run uvicorn
EXPOSE 9091
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9091", "--timeout-keep-alive", "180"]
