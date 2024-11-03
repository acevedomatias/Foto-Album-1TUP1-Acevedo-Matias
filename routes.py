from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Photo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    photos = Photo.query.all()
    return render_template('index.html', photos=photos)

@main.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        new_photo = Photo(title=title, description=description, image=image)
        db.session.add(new_photo)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('photo_form.html')

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    photo = Photo.query.get_or_404(id)
    if request.method == 'POST':
        photo.title = request.form['title']
        photo.description = request.form['description']
        photo.image = request.form['image']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('photo_form.html', photo=photo)

@main.route('/delete/<int:id>')
def delete(id):
    photo = Photo.query.get_or_404(id)
    db.session.delete(photo)
    db.session.commit()
    return redirect(url_for('main.index'))
