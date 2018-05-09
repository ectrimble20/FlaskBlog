# FlaskBlog
This is a learning project I built following a tutorial.

The is built with Python 3.6 using the Flask micro framework (a number of components) and SQLAlchemy along with a few other handy packages.

There's nothing super interesting going on yet, I plan to do some customization but I also plan to make a full-fledge web application based off what I've learned from this tutorial project.

Using this is pretty simple, if you're on Linux/Mac you'll need to export a few variables, if you're on Windows you'll want to use the 'set' command.

export FLASK_SECRET_KEY='somerandomchars'
export FLASK_DB_URI='sqlite:///site.db'
export FLASK_EMAIL_USER='my@email.com'
export FLASK_EMAIL_PASS='mysupersecretpassword'

again, if you're on Windows use "set" instead of export.

You can also go into the config.py file and set the variables there if you like being all insecure and what not.

Once you've got your Env Vars setup, you'll want to clone the repos using git clone URL_TO_REPO

I'd suggest doing this wherever you intend to run the app, you can move it around as you see fit though as the app paths relative to itself so you can't really break it with pathing.

You'll need to install a few packages with pip, specifically:
Flask, Flask-Bcrypt, Flask-Login, Flask-Mail, Flask-SQLAlchemy, Flask-WTF, Pillow

Installing the Flask-XXX package will handle installing dependencies, all those packages can be installed with:
pip install XXXX

Once you have the dependencies resolved, you can run the app with:
/usr/bin/python3.6 run.py   # obviously CD to the directory with run.py or link to it directory using something like readlink -f

Once the app is running, you can access it via localhost or 127.0.0.1, this can cause issues, so you might need to edit the run.
If you encounter errors, try adding the machines IP (if you're running it local) as the host argument for the app creation.

To do this, inside run.py, edit app.run(debug=True) to be app.run(debug=True, host="1.2.3.4")  
replacing 1.2.3.4 with your IP which you can find on Linux/Mac with ip addr show or ifconfig and with windows using ipconfig
