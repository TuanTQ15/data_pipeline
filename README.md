# data_pipeline
<!-- PREREQUISITES -->
## Prerequisites
Software required to run the project. Install:
- Ubuntu 20.04
- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.8+ (pip)](https://www.python.org/)
- [docker-compose](https://docs.docker.com/compose/install/)
<!-- RUNNING PROJECT -->
## Running project
*Note: if your machine's operating system is windows then you can use git bash to run the command
- Build project: 
         `docker-compose up -d mongo`,
         `docker exec -it mongo /usr/local/bin/init.sh`,
         `docker-compose up -d`
- Stop project: `docker-compose stop`

- Delete project: `docker-compose down`
- Delete volume: `docker volume rm $(docker volume ls -q)`
- Delete all image: `docker image rm -f $(docker image ls -q)`
- Delete all container: `docker rm -f $(docker ps -a -q)`
