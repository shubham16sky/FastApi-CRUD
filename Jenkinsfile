pipeline{
    agent any
    stages{
        stage('Git checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/shubham16sky/FastApi-CRUD.git'
            }
        }
        stage('Docker-compose up')
        {
            steps{
                sh './deployment.sh'
            }
        }
    }
}