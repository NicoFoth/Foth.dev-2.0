# 1) Base image
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 2) System deps (psql client etc. only if you need them)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 3) App directory
WORKDIR /app

# 4) Install Python deps
# (Adjust if you use poetry/pipenv; here I assume requirements.txt in repo)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copy project
COPY . .

# 6) Collect static (optional but typical for prod)
# ENV DJANGO_SETTINGS_MODULE=fothdev.settings  # adjust if your settings module differs
RUN python manage.py collectstatic --noinput || true

# 7) Expose Gunicorn port
EXPOSE 8000

# 8) Start app via Gunicorn
# Replace `fothdev.wsgi:application` with your actual wsgi module
CMD ["gunicorn", "webservice.wsgi:application", "--bind", "0.0.0.0:8000"]
