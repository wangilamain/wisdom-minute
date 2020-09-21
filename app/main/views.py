from flask import render_template, redirect,url_for
from . import main
from .forms import PitchForm, CommentForm, UpdateProfile
from ..models import *
from flask_login import current_user,login_user,login_required
from app  import db

@main.route('/')
def index():
    pitches = Pitch.get_pitches()
    title = 'Home'
    return render_template('index.html', pitches=pitches,title=title)

@main.route ('/new-pitch', methods =['GET','POST'])
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        content = form.content.data

        pitch = Pitch(title=title,category=category,user_id=current_user.id, content=content)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.new_pitch'))
    return render_template('new-pitch.html',form=form)

@main.route('/pitch/<int:id>',methods=['GET','POST'])
def pitch(id=None):
    if id:
        commentform=CommentForm()
        pitch = Pitch.get_pitch(id)
        comments = Comments.get_comments(id)

        if commentform.is_submitted():
            comment = Comments(comment=commentform.comment.data,user_id=current_user.id,pitch_id=id)
            db.session.add(comment)
            db.session.commit()
            return render_template('single-pitch.html',title=f'Pitch {id}',pitch=pitch,comments=comments,commentform=commentform)

        return render_template('single-pitch.html',title=f'Pitch {id}',pitch=pitch,comments=comments,commentform=commentform)

    return redirect(url_for('main.index'))

@main.route('/profile')
def profile():
     pitches = Pitch.get_user_pitches(current_user.id)

     return render_template('profile.html', pitches=pitches)