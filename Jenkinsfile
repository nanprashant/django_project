pipeline {
    agent any

    environment {
        PROJECT_NAME = 'My Django App'
        VENV_PATH = 'venv'
    }

    stages {
        stage('Preparation') {
            steps {
                echo 'Cleaning workspace...'
                deleteDir()
                echo 'Cloning repository...'
                git url: 'https://github.com/nanprashant/django_project.git', branch: 'feature/blog'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up virtual environment...'
                sh 'python3 -m venv venv'
                echo 'Activating virtual environment and installing requirements...'
                sh '''
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

                stage('Run Tests') {
            steps {
                echo 'Running tests...'
                
                sh './venv/bin/pytest'
            }
        }


        stage('Build & Collect Static Files') {
            steps {
                echo 'Collecting static files...'
                sh '''
                    . venv/bin/activate
                    python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying $PROJECT_NAME..."
                sh '''
                    . venv/bin/activate
                    # Add deployment script here
                    echo "Deployment done."
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
        always {
            echo '📦 Cleaning up workspace...'
            deleteDir()
        }
    }
}
