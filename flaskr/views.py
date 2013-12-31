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
        hashtag = request.form['hashtag']
        comment = request.form['comment']
        if not hashtag:
            raspi.tweet(comment)
            flash('Cheers ! you tweeted using #asahikawa_python')
        elif not '#' in hashtag:
            raspi.tweet(comment,('#'+hashtag))
            #tweet('#'+hashtag)
            flash('Congrats! you tweeted using #{hashtag}!'.format(
                hashtag = hashtag))
        else:
            raspi.tweet(comment,hashtag)
            flash('Congrats! you tweeted !')
    return redirect(url_for('index'))
