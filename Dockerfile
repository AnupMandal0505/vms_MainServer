# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /vms

# Install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .



# Collect static files
RUN python manage.py collectstatic --noinput



# Expose port for WebSocket
EXPOSE 8000


# Run Gunicorn (WSGI Server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core_backend.wsgi:application"]
