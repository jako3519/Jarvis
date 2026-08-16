FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt .
RUN pip3 install tensorflow pillow numpy

COPY . .

CMD ["python3", "imagemodel.py"]