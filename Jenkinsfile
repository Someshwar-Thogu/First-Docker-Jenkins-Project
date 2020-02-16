pipeline {
   agent any

   stages {
      stage('Hello') {
         steps {
            echo 'Hello World'
         }
      }
      stage('ls command') {
         steps {
            sh 'ls'
            echo "${env.WORKSPACE}"
         }
      }
      stage('Building Docker') {
         steps {
            sh "docker build -t Somesh -f ${env.WORKSPACE}/example-py-doctest/Dockerfile ${env.WORKSPACE}/example-py-doctest/"
         }
      }
    }
}
