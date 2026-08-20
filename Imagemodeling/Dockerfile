FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir \
    tensorflow==2.20.0 \
    keras==3.13.2 \
    pillow \
    numpy \
    opencv-python-headless \    
    paho-mqtt

COPY . .

CMD ["python3", "imagemodel.py"]