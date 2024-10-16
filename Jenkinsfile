pipeline {
	agent any
	    stages {
	        stage('Clone Repository') {
	        /* Cloning the repository to our workspace */
	        steps {
	        checkout scm
	        }
	   }
	   stage('Build Image') {
	   when {
                changeset "Dockerfile"
            }
	        steps {
	        bat 'docker build -t mynlpmodel:v1 .'
	        }
	   }
	   stage('Run Image') {
	        steps {
			
			bat 'docker stop nlpmodel || exit 0' 

			bat 'docker rm nlpmodel || exit 0'

			
	        bat 'docker run -d --name nlpmodel mynlpmodel:v1'
	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Testing.. the application'
	            }
	   }
	stage('master-branch-stuff') {
when {
  anyOf {
    changeset: "file1.txt"
    changeset: "file2.txt"
  }
}
    steps {
        echo 'run this stage - ony if file1 or file2 changes'
    }
}
    }
}
