# Flaskapp
Practice project for learning containerization, flask, python, terraform, and beyond.

# Built with
- Flask
- podman/docker
- Terraform

# Getting Started
To set up the project locally:
- Create Virtual Env
```
python3 -m venv flaskapp
```
- Initiate Virtual Env
```
source flaskapp/bin/activate
```
- Install dependencies
```
pip install -r requirements.txt
```
- Run Flask App
```
flask --app app.py run --host 0.0.0.0
```


To run project from docker: 
- Build Docker image
```
docker build . -t <tagname>
```
- Run Docker image
```
docker run --rm -d --env USER=$(whoami) --publish 5000:5000 public.ecr.aws/medirks/flaskapp:<tagname>
```

