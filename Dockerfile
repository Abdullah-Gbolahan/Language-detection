
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

# Use Render's dynamic port assignment
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]