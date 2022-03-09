# Khanah Backend
Khanah is a multi-vendor 
ecommerce application built around The New Boston Coin. 

## Contribute
To contribute to the **Khanah** mobile app you will need to:
- Clone the repository locally
- Create and activate a virtual environment
- Install the required libraries
- Create a postgres database
- Add the environment variables

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

#### Create and activate virtual environment
To isolate your dependencies and to avoid conflict with other
projects you have on your system it is advisable to create a
virtual environment.
```shell
> python -m venv venv
> venv/Scripts/actvate # Run this if you are on windows
> source venv/bin/activate # This if yoy are on linux or mac
```

#### Install required libraries
Now that you have activated your virtual environment it is time
to install the necessary libraries for you to start contributing.

If you check the root folder of the files you have just cloned
you will see a `requirements.txt` file. Open it, and you will see
a list of dependencies in this format `fastapi==0.75.0`. 

To install them run the command below in your terminal.
```shell
(venv) > pip install -r requirements.txt
```

> Noticed the `(venv)`?? That signifies that the virtual environment
> is activated. If you can't find it in your terminal make sure you go
> through step 2 again.

#### Create a postgres DB
To continue you will need to have Postgres installed. If you don't have
it installed yet follow [this tutorial](https://youtu.be/YysG13sFGok) 
to install it.

After installation open the pgadmin and create a new db called khanah
![PGAdmin Installation](https://d2o1p3wqepjvn9.cloudfront.net/media/uploads/2021/03/17/db-connection-gif.gif)


#### Add environment variable
Now it's time to add the environment variable for stuffs to work properly
run the command below in your terminal to duplicate `.env.example`
and rename the duplicate to `.env` or simply do that with your file 
manager.

```shell
(venv) > cp .env.example .env
```

> Edit the .env to fit your need

#### Run your project
```shell
(venv) > uvicorn app:app --reload
# if that doesn't work then run this
(venv) > python -m uvicorn app:app --reload
```