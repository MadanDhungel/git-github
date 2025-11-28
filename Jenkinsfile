pipeline {
    agent any

    environment {
        APP_ENV = 'development'
        Image_Name = 'Mygit'
        VERSION = '1.0.0'
        CONTAINER_NAME = 'mygit_container'
    }

    stages {
        stages('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scmGit(branches: [[name: 'master']],
                             userRemoteConfigs: [[url: 'https://github.com/MadanDhungel/git-github.git']])
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
                sh '
                docker build -t $Image_Name:$VERSION .
                '
            }
        }
        
        stage('Run Container') {
            steps {
                echo "Deploying container..."
                script {
                    // Stop old container if running
                    sh """
                    if [ \$(docker ps -aq -f name=${CONTAINER_NAME}) ]; then
    					docker rm -f ${CONTAINER_NAME}
		    		fi
					docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Verifying the app is running..."
                script {
                    sh "docker ps | grep ${CONTAINER_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build and deployment successful!"
        }
        failure {
            echo "❌ Build or deployment failed!"
        }
    }
}