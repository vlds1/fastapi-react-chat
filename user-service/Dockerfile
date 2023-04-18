FROM python:3.10.0

RUN mkdir /src

WORKDIR /src

COPY req.txt .

RUN python -m pip install --upgrade pip

RUN pip3 install -r ./req.txt --no-cache-dir

COPY . .
