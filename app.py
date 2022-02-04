"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User, Post


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route("/")
def homepage():
    users = User.query.all()
    return render_template('home.html', users= users)

@app.route('/adduser')
def adduserpage():

    return render_template('adduser.html')

@app.route('/adduser', methods=["POST"])
def addnewuser():
    
    firstname= request.form['firstname']
    lastname=request.form['lastname']
    imageurl=request.form['url']
    
    user = User(first_name = firstname, last_name = lastname, image_url = imageurl or None )
    db.session.add(user)
    db.session.commit()
    
    return redirect(f'/{user.id}')

@app.route('/<int:user_id>')
def show_user_page(user_id):
    
    user = User.query.get_or_404(user_id)
    return render_template('userdetail.html', user = user)

@app.route('/<int:user_id>/delete', methods=['POST'])
def delete_page(user_id):
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    return redirect('/')

@app.route('/<int:user_id>/edit')
def edit_page(user_id):
    user = User.query.get_or_404(user_id)

    return render_template('edit.html',user=user)

@app.route('/<int:user_id>/edit', methods=['POST'])
def update_page(user_id):
    user = User.query.get_or_404(user_id)
    user.firstname= request.form['firstname']
    user.lastname=request.form['lastname']
    user.imageurl=request.form['url']
    
    db.session.add(user)
    db.session.commit()
    
    return redirect('/')

@app.route('/<int:user_id>/addpost')
def addpost_page(user_id):
    
    return render_template('addpost.html')

@app.route('/<int:user_id>/addpost', methods=["POST"])
def addnewuser_page(user_id):
    
    newtitle= request.form['title']
    newcontent=request.form['content']
    
    post = Post(title = newtitle, content = newcontent, user_id =user_id)
    db.session.add(post)
    db.session.commit()
    
    return redirect(f'/{user_id}')


@app.route('/<int:user_id>/<int:post_id>')
def show_post_page(user_id,post_id):
    
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', user = user,post=post)


@app.route('/<int:user_id>/<int:post_id>/edit')
def edit_post_page(user_id,post_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    return render_template('postedit.html',user=user,post=post)

@app.route('/<int:user_id>/<int:post_id>/edit', methods=['POST'])
def update_post_page(user_id,post_id):
    post = Post.query.get_or_404(post_id)
    post.newtitle= request.form['title']
    post.newcontent=request.form['content']
    
    db.session.add(post)
    db.session.commit()
    
    return redirect(f'/{user_id}')

@app.route('/<int:user_id>/<int:post_id>/delete', methods=['POST'])
def delete_post_page(user_id,post_id):
    
    post=Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    
    return redirect(f'/{user_id}')