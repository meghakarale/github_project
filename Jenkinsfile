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
	        steps {
	        bat docker build -t mynlpmodel:v1 .'
	        }
	   }
	   stage('Run Image') {
	        steps {
	        bat docker run -d -p 5000:4000 --name nlpmodel mynlpmodel:v1'
	        }
	   }
	   stage('Testing'){
	        steps {
	            echo 'Testing..'
	            }
	   }
    }
}