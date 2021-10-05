# data_pipeline
<!-- PREREQUISITES -->
## Prerequisites
Software required to run the project. Install:
- Windows or Ubuntu 20.04
- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.8+ (pip)](https://www.python.org/)
- [docker-compose](https://docs.docker.com/compose/install/)
<!-- RUNNING PROJECT -->
## Running project
- Build project: `docker-compose up`

- Stop project: `docker-compose stop`

- Delete project: `docker-compose down`
- Delete volume: `docker volume rm $(docker volume ls -q)`
- Delete all image: `docker image rm -f $(docker image ls -q)`
*Note: if your machine's operating system is windows then you can use git bash to run the command