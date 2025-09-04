From python:3.9
copy . /App
workdir /App
run pip install -r requirements.txt
cmd ["python", "app.py"]
expose 5000

#docker build -t myflaskapp .
