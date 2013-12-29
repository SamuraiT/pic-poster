from flask import request, redirect, url_for, render_template, flash
from flaskr  import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweet/',methods = ['POST'])
def tweet():
    if request.method == 'POST':
        hastag = request.form['hastag']
        if not hastag:
            flash('Cheers ! you tweeted using #asahikawa_python')
        elif not '#' in hastag:
            #tweet('#'+hastag)
            flash('Congrats! you tweeted using #{hastag}!'.format(
                hastag = hastag))
        else:
            flash('Congrats! you tweeted !')
    return redirect(url_for('index'))

