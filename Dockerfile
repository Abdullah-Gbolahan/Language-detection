
# Use Python 3.11 slim for better performance and smaller image size
FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Copy requirements first for better Docker layer caching
COPY ./requirements.txt /code/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code
COPY . /code

 
# Expose port (Render will override this with $PORT)
EXPOSE 8000

# Use dynamic port assignment for Render
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app