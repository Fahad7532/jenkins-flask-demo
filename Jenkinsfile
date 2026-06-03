pipeline {
    agent any

    environment {
        IMAGE_NAME = 'jenkins-flask-demo'
        CONTAINER_NAME = 'jenkins-flask-demo-container'
        APP_PORT = '5001'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests inside Python Docker container...'
                sh '''
                    docker run --rm \
                    -v "$PWD":/app \
                    -w /app \
                    python:3.11-slim \
                    sh -c "pip install -r requirements.txt && pytest"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                    docker tag $IMAGE_NAME:$BUILD_NUMBER $IMAGE_NAME:latest
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Deploying application container...'
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true

                    docker run -d \
                    --name $CONTAINER_NAME \
                    -p $APP_PORT:5000 \
                    $IMAGE_NAME:latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Checking running containers...'
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. Application is deployed.'
        }

        failure {
            echo 'Pipeline failed. Check the stage where the error happened.'
        }
    }
}
