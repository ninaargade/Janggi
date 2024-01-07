# Janggi

The following **Python** program contains a class that executes the game Janggi, which is the Korean version of chess. The program represents the backend of the game, where there is a way for keeping track of the game board, game pieces, player turns, and game state. There is a method to make a move which takes in algebraic notation coordinates representing spaces on the board. There are many various helper functions that execute game play, and finally, there are methods to verify if a player is in check or checkmate, which indicates if the game has been won.

You can read more about Janggi and game play rules [here](https://en.wikipedia.org/wiki/Janggi).

There is a **Jenkins** pipeline included in a Jenkinsfile to ensure proper technique for continuous delivery while developing the back-end. Using Jenkins, we can evaluate the unit tests in unitTests.py as we build the back-end of the game incrementally. The unitTests.py file utilizes the Python unitests framework and contains a test suite of valid player "moves." As we build our game and commit our changes, we can add corresponding tests and use Jenkins to ensure that we are writing valid code to our main branch.

# Instructions to run Jenkins Pipeline:

1. Install Docker on your local machine.
2. Run this command: 

    ``docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11``

3. Write down the password that is created during this first time set up process.

4. Go to localhost:8080 and enter password.

5. Create a new Jenkins pipeline using this repository's Jenkinsfile for the pipeline script.

6. While the docker container is running, run cmd: 

    ``docker ps`` to see what containers are running - copy the container ID for Jenkins, like ``8f7c957e19fd``

7. Run command: 

    ``docker exec -it -u 0 8f7c957e19fd /bin/bash`` to open an interactive terminal within the Docker Container as root (user 0)

8. Run command(s): 

    ``apt-get update`` and ``apt-get install python3`` and ``apt-get install python3-pip`` to install Python3 and pip within the Docker container

9. Every time a change is committed to either Janggi.py or the unitTests.py file, run the "Build Now" button in Jenkins to see results for the "checkout", "build", and "test" stages of the pipeline. 

10. From here, you can assess the logs to see if a part of the pipeline failed and troubleshoot from there. It is recommended to create a separate branch with changes and merge this branch into main *only* after the pipeline is sucessful for all stages.


