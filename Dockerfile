FROM nvcr.io/nvidia/l4t-tensorflow:r36.4.0-tf2-py3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "imagemodel.py"]