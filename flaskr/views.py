from flask import request, redirect, url_for, render_template, flash
from flaskr  import app
from picbot.manage import Photographer,OverChar,HASH_TAG
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweet/',methods = ['POST'])
def tweet():
    if request.method == 'POST':
        raspi = Photographer()
        hashtag = request.form['hashtag']
        comment = request.form['comment']
        post_a_pic(raspi,comment,hashtag)
    return redirect(url_for('index'))

def post_a_pic(raspi,comment=u'',hashtag=HASH_TAG):
    if not hashtag:
        try:
            raspi.tweet(comment)
            flash('Cheers ! you tweeted using #asahikawa_python')
        except OverChar as e:
            flash(str(e))
    elif not '#' in hashtag:
        try:
            raspi.tweet(comment,('#'+hashtag))
            flash('Congrats! you tweeted'
                ' using #{hashtag}!'.format(
                hashtag = hashtag))
        except OverChar as e:
            flash(str(e))
    else:
        try:
            raspi.tweet(comment,hashtag)
            flash('Congrats! you tweeted !')
        except OverChar as e:
            flash( str(e) )

