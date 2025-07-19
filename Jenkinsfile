pipeline {
    agent any

    environment {
        IMAGE_NAME = "chaitanya1003/employee-count"
        DOCKERHUB_USER = "yourdockerhubusername"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Chaitanya10912/employee-count-tracker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("%{IMAGE_NAME}%")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                            docker.image("%{IMAGE_NAME}%").push("latest")
                        }
                    }
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                bat 'docker-compose down || true'
                bat 'docker-compose up -d --build'
            }
        }
    }
}
