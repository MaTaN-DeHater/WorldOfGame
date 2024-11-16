pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'matanx/wog'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                git branch: 'master', url: 'https://github.com/Matan-Shabi/WorldOfGame.git'
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    echo 'Running Docker container...'
                    bat """
                    docker run -d -p 8777:5000 -v "${WORKSPACE}\\scores.json:/app/scores.json" --name WorldOfGame ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running Selenium tests...'
                    bat 'python tests/e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
            echo 'Stopping Docker container...'
            bat 'docker stop WorldOfGame'
            bat 'docker rm WorldOfGame'

            withCredentials([usernamePassword(credentialsId: 'dockerhub_credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                echo 'Logging in to Docker Hub...'
                bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"

                echo 'Pushing Docker image to DockerHub...'
                bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker resources...'
            bat 'docker system prune -f'
        }
    }
}
