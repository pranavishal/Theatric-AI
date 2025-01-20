# Use Python image

FROM python:3.10-slim


# Set working directory
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt /app/requirements.txt


# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy backend app code from the current directory
COPY . /app

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

