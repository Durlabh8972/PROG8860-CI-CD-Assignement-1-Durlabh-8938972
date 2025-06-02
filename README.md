# Assignment 1 - CI/CD Pipeline with GitHub Actions

## 🔧 Technology Used
- Python 3.9
- Flask
- Docker
- GitHub Actions

## 🛠️ Steps Followed
1. Created a separate branch for the assignment.
2. Added a Flask application with multiple endpoints.
3. Wrote a Dockerfile to containerize it.
4. Added GitHub Actions CI pipeline triggered on pull request.

## 🚀 CI Stages
- **Build**: Install dependencies.
- **Test**: Run unit tests.
- **Dockerize**: Build Docker image.
- **Run**: Start container and show it.
- **Stop**: Stop the container.

## ✅ STEP 1: RUN THE FLASK APP LOCALLY
Open terminal in the project root folder.

pip install flask

python run.py

## ✅ STEP 2: Open browser and run the below application links.

http://localhost:5000

http://localhost:5000/health

## Application Screenshots

<img width="950" alt="image" src="https://github.com/user-attachments/assets/d0434b39-1f58-4e79-94cc-14e1d6a7d7c5" />


<img width="959" alt="image" src="https://github.com/user-attachments/assets/5608f380-bca8-4c40-8619-5a3cb15c4c77" />

## ✅ STEP 3: RUN UNIT TESTS LOCALLY
Run this command: python -m unittest discover test

<img width="949" alt="image" src="https://github.com/user-attachments/assets/cd79ecde-7d2f-4c1d-92b3-a89575ce7ffb" />

## ✅ STEP 4: BUILD DOCKER IMAGE
Run this command: docker build -t durlabh-flask-app .

<img width="959" alt="image" src="https://github.com/user-attachments/assets/70e2a8ce-315a-4d94-bd69-4a3d626a3508" />

## ✅ STEP 5: RUN DOCKER CONTAINER
Run this command: docker run -d -p 5000:5000 --name flask_container durlabh-flask-app

<img width="955" alt="image" src="https://github.com/user-attachments/assets/4307c51f-7e34-4e5e-855c-24eadca4dd54" />

<img width="950" alt="image" src="https://github.com/user-attachments/assets/abd99c2f-4ffb-4434-a1cb-19114a69bed8" />

## ✅ STEP 6: CI/CD Pipeline

<img width="959" alt="image" src="https://github.com/user-attachments/assets/a2a0b7d4-b39b-49e4-a5d9-a562bf856f9d" />


## ✅ STEP 7: GitHub Actions Workflow Successful

<img width="959" alt="image" src="https://github.com/user-attachments/assets/b49fc1f5-de50-494a-a10c-f4e19f1a4e50" />









