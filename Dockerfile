FROM --platform=linux/amd64 python:3.8

WORKDIR /app
RUN mkdir -p contracts

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
