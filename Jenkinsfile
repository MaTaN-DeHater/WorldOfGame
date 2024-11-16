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
                    branch: 'master', url: 'https://github.com/Matan-Shabi/WorldOfGame.git'
                }
            }
        }

        stage('Build') {
            steps {
                 echo 'Building Docker image...'
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
            }
        }

        stage('Run') {
            steps {
                script {

                    echo 'Running Docker container...'

                    bat """
                    docker run -d -p 8777:8777 -v \"${pwd()}/scores.json\":/scores.json --name score_app ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
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
