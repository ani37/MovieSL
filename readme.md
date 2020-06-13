# Movie shooting location finder
#### The task is to build a web app that helps them find out shooting locations of their favorite movies.


```
directory_tree :
```

```
Task
├── task_main.py
├── README.md
├── .vscode
│   └── settings.json
├── requirements.txt
├── static
│   ├── main.css
│   └── search.js
├── templates
│   ├── index.html
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   └── search.html
├── forms.py
├── data.json
├── __pycache__
│   ├── data.cpython-38.pyc
│   └── forms.cpython-38.pyc
└──  Pipfile

```
#### Dependencies:

arrow==0.15.6

binaryornot==0.4.4

certifi==2020.4.5.2

chardet==3.0.4

click==7.1.2

cookiecutter==1.7.2

dnspython==1.16.0

email-validator==1.1.1

Flask==1.1.2

Flask-SQLAlchemy==2.4.3

Flask-WTF==0.14.3

idna==2.9

itsdangerous==1.1.0

Jinja2==2.11.2

jinja2-time==0.2.0

MarkupSafe==1.1.1

poyo==0.5.0

python-dateutil==2.8.1

python-slugify==4.0.0

requests==2.23.0

six==1.15.0

SQLAlchemy==1.3.17

text-unidecode==1.3

urllib3==1.25.9

Werkzeug==1.0.1

WTForms==2.3.1


# 1. MovieLens Dataset Description
If you love movies, and you love San Francisco, you're bound to love this -- a listing of filming locations of movies shot in San Francisco starting from 1924. You'll find the titles, locations, fun facts, names of the director, writer, actors, and studio for most of these films.


### 1.1 Dataset
The initial dataset is taken from [https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am](https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am)

Dataset via SODA API : [https://data.sfgov.org/resource/yitu-d5am.json](https://data.sfgov.org/resource/yitu-d5am.json)

#### 1.2 Dataset Description
>If you love movies, and you love San Francisco, you're bound to love this -- a listing of filming locations of movies shot in San Francisco starting from 1924. You'll find the titles, locations, names of the director, writer, actors, and studio for most of these films.


# 2. Movie shooting location finder
After scraping and storing the data in mongoDB, three algorithms were utilised to predict the ratings for the particular user in consideration and top 10 movies were displayed.
It is suggested that the user rate at least 20 of the movies, effectively taking the value of K as 20. This value is taken considering that All selected users had rated at least 20 movies as written in the README section of the MovieLens Dataset.

### 2.1. Dynamic Search Interface
In UUCF the main idea is that, the algorithm finds the User's most similar to the current User and calculates the ratings of the movies he has not rated by the similarity score. The similarity is based on Pearson Correlation.
### 2.2. Listing all movies
In IICF the algorithm selects the movies most closest to the movies the user has already rated and takes this similarity score and ratings of the movies the user has rated into consideration and gives suggestions based on the highest ratings predicted. The similarity is based on Pearson Correlation.
### 2.3. Login/ Signup
The strength of matrix factorization is the that it can gather information that are not seen directly but can be visualized by analyzing user's behavior. Using this criteria we can judge the user's opinion regarding th particular movie. This method is the most viable option for recommender systems.

# 3. Deploying to He roku
The project was deployed to Heroku, by integrating it with GitHub the link to the website is [https://moviers.herokuapp.com/](https://moviers.herokuapp.com/)

### 3.1. Flask
For the backend of this project Flask was used. Flask is a micro web framework written in Python.

### 3.2. Gunicorn
The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server.  Since Flask cannot serve multiple users at the same time, we serve the application using Gunicorn. 


# 4. Docker Container
The `Dockerfile`  is included in the root of this repository, and can be build from within this directory using:

```
docker build --tag=moviers .
```

and then run:
```
docker run -p 5000:5000 moviers
```
to map the port `5000` of the docker container to your machines port: `5000` this can be easily conffigured as per your requirements.  Then visit `localhost:5000` in your web-browser.




<br>
<br>
<br>
<br>
<br>
<br>
<br>



Authored By: Aniket Agarwalla

Department of Computer Science and Engineering <br>
National Institute of Technology Silchar <br>

[https://ani37.github.io/](https://ani37.github.io/)
