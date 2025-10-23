# Flaskapp
Practice project for learning containerization, flask, python, terraform, and beyond.

# Built with
- Flask
- podman/docker
- Terraform

# Getting Started
To set up the project locally:
```
python3 -m venv flaskapp
```
```
source flaskapp/bin/activate
```
```
pip install -r requirements.txt
```
```
flask --app app.py run --host 0.0.0.0
```


To run project from docker: 
```
docker build . -t <tagname>
```
```
docker run --rm -d --env USER=$(whoami) --publish 5000:5000 public.ecr.aws/medirks/flaskapp:0.0.1-61ab865
```

