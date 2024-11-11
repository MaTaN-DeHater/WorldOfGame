pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'matanx/wog:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm

                dir('WorldOfGame') {
                    git url: 'https://github.com/MaTaN-DeHater/WorldOfGame.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run('-d -p 8777:5000 -v $WORKSPACE/scores.json:/app/scores.json')
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python tests/e2e.py', returnStatus: true)
                    if (result != 0) {
                        error('Tests failed')
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop $(docker ps -q --filter ancestor=' + DOCKER_IMAGE + ')'
                    sh 'docker push ' + DOCKER_IMAGE
                }
            }
        }
    }
}
