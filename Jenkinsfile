pipeline {
   
    agent any    
        
    triggers {
    cron('* * * * *')
  }

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
                    docker run --rm -v $PWD:/app -w /app python:3.10-slim bash -c "
                        python3 -m venv venv &&
                        source venv/bin/activate &&
                        pip install --upgrade pip &&
                        pip install selenium pytest pytest-html webdriver-manager &&
                        pytest --html=report.html --self-contained-html
                    "
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p reports
                    . $VENV_DIR/bin/activate
                   PYTHONPATH=. pytest --junitxml=reports/test-results.xml
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

