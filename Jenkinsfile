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
            echo ${env.WORKSPACE}
         }
      }
    }
}
