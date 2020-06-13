# Movie shooting location finder
#### The task is to build a web app that helps them find out shooting locations of their favorite movies.


```
directory_tree :

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

#### Stack
*Python, Flask, jQuery, AJAX, JSON, Jinja, HTML, CSS, JavaScript, Bootstrap, SQLAlchemy*


#### Dependencies:

arrow==0.15.6 <br>
binaryornot==0.4.4 <br>
certifi==2020.4.5.2 <br>
chardet==3.0.4 <br>
click==7.1.2 <br>
cookiecutter==1.7.2 <br>
dnspython==1.16.0 <br>
email-validator==1.1.1 <br>
Flask==1.1.2 <br>
Flask-SQLAlchemy==2.4.3 <br>
Flask-WTF==0.14.3 <br>
gunicorn==20.0.4 <br>
idna==2.9 <br>
itsdangerous==1.1.0 <br>
Jinja2==2.11.2 <br>
jinja2-time==0.2.0 <br>
MarkupSafe==1.1.1 <br>
poyo==0.5.0 <br>
python-dateutil==2.8.1 <br>
python-slugify==4.0.0 <br>
requests==2.23.0 <br>
six==1.15.0 <br>
SQLAlchemy==1.3.17 <br>
text-unidecode==1.3 <br>
urllib3==1.25.9 <br>
Werkzeug==1.0.1 <br>
WTForms==2.3.1 <br>


# 1. Dataset Description
If you love movies, and you love San Francisco, you're bound to love this -- a listing of filming locations of movies shot in San Francisco starting from 1924. You'll find the titles, locations, names of the director, writer, actors, and studio for most of these films.


### 1.1 Dataset
The initial dataset is taken from [https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am](https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am)

Dataset via SODA API : [https://data.sfgov.org/resource/yitu-d5am.json](https://data.sfgov.org/resource/yitu-d5am.json)

# 2. Movie shooting location finder
 Movie shooting location finder is a web application that displays a list of all movies shooted at a location along with some other details about a movie. It also provides a text search bar for dynamically searching users favourate movies by title.
 
### 2.1. Dynamic Search Interface
In this project we build a simple Search bar that searches for movies in JSON file with some prefix dynamically using the Fetch API, Async/Await, Regex and high order array methods. 

*Note : Movies can only be retrieved if they are available in the dataset.*

### 2.2. Listing all the movies
Here, we loop over the file and we post the titles, locations, names of the director and writer for most of these films. Undefined locations are checked and are ignored from the list.

### 2.3. Login/ Signup
 WTForms are used for Login/ Signup.It is a flexible forms validation and rendering library for Python web development. It can work with any web framework and template engine you choose. 
 
 *Note : Database for login signup is ignored as currently there is no role of users.*

# 3. Deploying to pythonanywhere
PythonAnywhere is an online integrated development environment and web hosting service based on the Python programming language.
The link to the website is [ani37.pythonanywhere.com](http://ani37.pythonanywhere.com/)

### 3.1. Flask
For the backend of this project Flask was used. Flask is a micro web framework written in Python.

# 4. Instructions to execute:
```
1. Installing pip

Windows :
py -m pip --version
pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)
py -m pip install --upgrade pip 

Linux & Mac : 
python3 -m pip install --user --upgrade pip 
 ```
 ```
2. Installing virtualenv 

Windows :
py -m pip install --user virtualenv 

Linux & Mac :
python3 -m pip install --user virtualenv 
```
 ```
3. Installing virtualenv & activate

Windows :
py -m venv env 
.\env\Scripts\activate

Linux & Mac :
python3 -m venv env 
source env/bin/activate
```
 ```
4. Clone git repo
git clone https://github.com/ani37/movie-shooting-location-finder.git
cd movie-shooting-location-finder
```
 ```
5. Install requirements.txt
pip install -r requirements.txt
```
 ```
6. Start web server
python task_main.py
```


<br>
<br>
<br>


Authored By: Aniket Agarwalla

Department of Computer Science and Engineering <br>
National Institute of Technology Silchar <br>

[https://ani37.github.io/](https://ani37.github.io/)
