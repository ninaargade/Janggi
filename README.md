# Janggi
___

The following program contains a class that executes the game Janggi, which is the Korean version of
chess. The program represents the backend of the game, where there is a way for keeping track of the game board, game pieces, player turns, and game state. There is a method to make a move which takes in algebraic notation coordinates representing spaces on the board. There are many various helper functions that execute game play, and finally, there are methods to verify if a player is in check or checkmate, which indicates if the game has been won.

You can read more about Janggi and game play rules [here](https://en.wikipedia.org/wiki/Janggi)

# Instructions to run Jenkins Pipeline:
___

1. Install Docker on your local machine.
2. Run this command: 

docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11

3. Write down the password that is created during this first time set up process.

4. Go to localhost:8080 and enter password.

5. While the docker container is running, run cmd: 

docker ps to see what containers are running - copy the container ID for Jenkins, like 8f7c957e19fd

6. Run command: docker exec -it -u 0 8f7c957e19fd /bin/bash to open an interactive terminal within the Docker Container as root (user 0)

7. Run command: apt-get update and apt-get install python3 and apt-get install python3-pip to install Python3 and pip within the Docker container

8. Every time a unit test is committed to the unitTests.py file, run the "Build Now" button to see results for the "checkout", "build", and "test" stages of the pipeline.


