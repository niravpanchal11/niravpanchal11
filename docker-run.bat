@echo off
REM Build Docker image
echo Building Docker image...
docker build -t nirav-portfolio .

REM Run Docker container
echo Starting container...
docker run -p 8000:8000 --env-file .env nirav-portfolio
