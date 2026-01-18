# -------- Base image --------
FROM python:3.13-slim

# -------- Environment --------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -------- Work directory --------
WORKDIR /app

# -------- System dependencies --------
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2 \
    libxslt1.1 \
    && rm -rf /var/lib/apt/lists/*

# -------- Python dependencies --------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------- Copy application --------
COPY app ./app

# -------- Expose port --------
EXPOSE 8000

# -------- Run app --------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
