FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port
EXPOSE 8000

# Make wait-for-db.sh executable
RUN chmod +x wait-for-db.sh

# Run the application with wait-for-db.sh to ensure DB is ready
CMD ["./wait-for-db.sh", "db", "5432", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
