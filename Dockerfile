# Multi-stage Dockerfile for StyleForge AI

# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are accessible
ENV PATH=/root/.local/bin:$PATH

# Create non-root user
RUN useradd -m -u 1000 styleforge && \
    mkdir -p /app/output /app/temp /app/logs && \
    chown -R styleforge:styleforge /app

USER styleforge

# Copy application code
COPY --chown=styleforge:styleforge . .

# Create necessary directories
RUN mkdir -p /home/styleforge/.cache/replicate

# Expose port if API server is added
# EXPOSE 8000

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    OUTPUT_DIR=/app/output \
    TEMP_DIR=/app/temp

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Default command
CMD ["python", "styleforge.py", "--help"]

# If running as API server:
# CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
