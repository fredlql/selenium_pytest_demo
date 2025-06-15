pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install selenium pytest pytest-html webdriver-manager
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p reports
                    . $VENV_DIR/bin/activate
                    pytest --junitxml=reports/test-results.xml
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.png', allowEmptyArchive: true
            junit 'reports/test-results.xml'
        }
    }
}

