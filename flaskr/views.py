from flask import request, redirect, url_for, render_template, flash
from flaskr  import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweet/',methods = ['POST'])
def tweet():
    if request.method == 'POST':
        if not request.form['hastag']:
            flash('Cheers ! you tweeted using #asahikawa_python')
        else:
            flash('Congrats! you tweeted !')
        # tweet
    return redirect(url_for('index'))

