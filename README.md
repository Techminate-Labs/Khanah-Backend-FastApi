# Khanah Backend
Khanah is a multi-vendor
ecommerce application built around The New Boston Coin.

## Contribute
To contribute to the **Khanah** mobile app you will need to:
- Clone the repository locally
- Edit the environment variable
- Build and run the docker image
- Migrate the database

#### Clone the project
To clone this project you will navigate to
the directory you would love to clone to using the terminal
or command prompt and the run the command below in your terminal.
```shell
> git clone https://github.com/Techminate/Khanah-Backend-FastApi.git <folder-name>
> cd folder name
```
> Don't forget to change <folder_name> to the name you want to
> clone the project too.

#### Add environment variable
Now it's time to add the environment variable for stuffs to work properly
run the command below in your terminal to duplicate `.env.example`
and rename the duplicate to `.env` or simply do that with your file
manager.

```shell
(venv) > cp .env.example .env
```

> Edit the .env to fit your need


#### Build and run the docker image
```shell
> docker-compose up -d --build
> docker-compose up
```

#### Migrate the database
To migrate the database you will need to enter an interactive
shell in your docker container

First, open up a new terminal window or tab.
Then get the IDs of all running processes like so:
```shell
docker ps
```

You should see an output that
starts with something that looks like the following:


```shell
CONTAINER ID      IMAGE
a123bc007edf      phresh_server
867g5309hijk      postgres:12.1-alpine
```

Copy the ID of the container running our server. In this example
that would be **a123bc007edf**. Now we can start
executing bash commands as the container's root use by typing:

```shell
docker exec -it a123bc007edf bash
```

The -it part indicates we want to use the container interactively so
we can run commands and inspect the container. By default,
Docker containers run and exit as soon as they've finished executing.

Inside the bash shell, we can start exploring a little bit.

```shell
ls
```

We should see all of the files and directories that Docker
has copied into our container.

```shell
Dockerfile    alembic.ini     app      requirements.txt     tests
```

Run the migration
```shell
alembic upgrade head
```

We should see an output indicating that our db has been migrated like
below:
```shell
INFO   [alembic.runtime.migration] Running upgrade  -> 12345678654 ...
```


#### Run your project
```shell
(venv) > uvicorn app:app --reload
# if that doesn't work then run this
(venv) > python -m uvicorn app:app --reload
```
