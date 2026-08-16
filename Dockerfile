FROM nvcr.io/nvidia/l4t-tensorflow:r35.3.1-tf2-py3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "imagemodel.py"]