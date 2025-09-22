from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import User
from extensions import db, login_manager

bp = Blueprint('auth_routes', __name__)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@bp.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		confirm_password = request.form['confirm_password']
		full_name = request.form['full_name']
		phone = request.form['phone']
		address = request.form['address']

		if User.query.filter_by(username=username).first():
			flash('Username already exists.')
			return redirect(url_for('auth_routes.register'))
		if User.query.filter_by(email=email).first():
			flash('Email already registered.')
			return redirect(url_for('auth_routes.register'))
		if password != confirm_password:
			flash('Passwords do not match.')
			return redirect(url_for('auth_routes.register'))

		hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
		new_user = User(
			username=username,
			email=email,
			password=hashed_pw,
			full_name=full_name,
			phone=phone,
			address=address
		)
		db.session.add(new_user)
		db.session.commit()
		flash('Registration successful. Please log in.')
		return redirect(url_for('auth_routes.login'))
	return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		user = User.query.filter_by(username=username).first()
		if user and check_password_hash(user.password, password):
			login_user(user)
			return redirect(url_for('account_routes.account'))
		else:
			flash('Invalid username or password.')
	return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth_routes.login'))
