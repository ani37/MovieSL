from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '96f27dd98246d36e1eb5de8b20134e25'





with open("data.json", encoding='utf8') as f:
    posts = json.load(f)

# Note krna : if decoding of the data fails, that's because you didn't tell the open() call what codec
#  to use when reading the file; add the correct codec with an encoding argument:
# otherwise the file will be opened with your system default codec, which is OS dependent.



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',posts = posts)
    
@app.route("/search")
def search():
    return render_template('search.html',title ='search')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        #else:
         #   flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title ='Register',form = form)

if __name__ == '__main__': 
    app.run(debug=True)