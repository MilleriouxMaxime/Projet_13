# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Collect static files (optional, uncomment if you want to collect at build time)
# RUN python manage.py collectstatic --noinput

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Start server
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"] 