pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'matanx/wog:latest'
        CONTAINER_NAME = 'wog_container'
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
                   
                    bat "docker build -t ${DOCKER_IMAGE} WorldOfGame"
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    
                    bat "docker rm -f ${CONTAINER_NAME} || true"

                   
                    bat "docker run -d --name ${CONTAINER_NAME} -p 8777:5000 -v %WORKSPACE%\\scores.json:/app/scores.json ${DOCKER_IMAGE}"
                }
            }
        }

       
        stage('Test: Scores Service') {
            steps {
                script {
                   
                    def result = bat(script: "docker exec ${CONTAINER_NAME} python -c 'from WorldOfGame.tests.e2e import test_scores_service; exit(0) if test_scores_service(\"http://localhost:5000\") else exit(1)'", returnStatus: true)
                    if (result != 0) {
                        error('Scores Service test failed')
                    }
                }
            }
        }

        stage('Test: Wipe Scores Button') {
            steps {
                script {
                   
                    def result = bat(script: "docker exec ${CONTAINER_NAME} python -c 'from WorldOfGame.tests.e2e import test_wipe_scores_button; exit(0) if test_wipe_scores_button(\"http://localhost:5000\") else exit(1)'", returnStatus: true)
                    if (result != 0) {
                        error('Wipe Scores Button test failed')
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                  
                    bat "docker stop ${CONTAINER_NAME} || true"
                    bat "docker rm ${CONTAINER_NAME} || true"

                    
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        bat "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
    }

   
    post {
        always {
            script {
                
                bat "docker stop ${CONTAINER_NAME} || true"
                bat "docker rm ${CONTAINER_NAME} || true"
            }
        }
    }
}
