pipeline {
	agent any
	    stages {
	        stage('Clone Repository') {
	        /* Cloning the repository to our workspace */
	        steps {
	        checkout scm
	        }
	   }
	   

        stage('split_data') {
		when {
  anyOf {
    changeset "flower_data.csv"
    
  }
  }
            steps {
                echo 'Running split datajob'
                build 'splitdata'
                }
            }
			

        stage('train') {
		when {
  anyOf {
    changeset "params.yaml"
    changeset "flower_data.csv"
  }
  }
            steps {
                echo 'Running train job'
                build 'train'
                }
            }
			
        stage('evaluate') {
		when{
		anyOf {
    changeset "params.yaml"
    changeset "flower_data.csv"
  }
  }
            steps {
                echo 'Running evaluate Job'
                build 'evaluate'
                 }
            }
	   	   
	   stage('Build Image') {
	   when {
	   anyOf {
                changeset "Dockerfile"
				changeset "params.yaml"
				changeset "flower_data.csv"
            }
			}
	        steps {
	        bat 'docker build -t irismodel:v1 .'
	        }
	   }
	   stage('Run Image') {
	        steps {
			
			bat 'docker stop irismodelc || exit 0' 

			bat 'docker rm irismodelc || exit 0'

			
	        bat 'docker run -d -p 8005:8005 --name irismodelc irismodel:v1'
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
    changeset "file1.txt"
    changeset "file2.txt"
  }
}
    steps {
        echo 'run this stage - ony if file1 or file2 changes'
    }
}




}
}
