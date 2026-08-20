FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    libxcb1 \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libegl1 \
    libgles2 \
    mesa-common-dev \
    libegl1-mesa \
    libgles2-mesa \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir \
    tensorflow==2.20.0 \
    keras==3.13.2 \
    pillow \
    numpy \
    opencv-python-headless \
    paho-mqtt \
    mediapipe
COPY . .
CMD ["python3", "imagemodel.py"]