from flask import request, redirect, url_for, render_template, flash
from flaskr  import app
from picbot.manage import Photographer
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweet/',methods = ['POST'])
def tweet():
    if request.method == 'POST':
        raspi = Photographer()
        hastag = request.form['hastag']
        comment = request.form['comment']
        if not hastag:
            raspi.tweet(comment)
            flash('Cheers ! you tweeted using #asahikawa_python')
        elif not '#' in hastag:
            raspi.tweet(comment,('#'+hastag))
            #tweet('#'+hastag)
            flash('Congrats! you tweeted using #{hastag}!'.format(
                hastag = hastag))
        else:
            raspi.tweet(comment,hastag)
            flash('Congrats! you tweeted !')
    return redirect(url_for('index'))

