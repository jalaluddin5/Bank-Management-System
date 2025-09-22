from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import User, Transaction
from extensions import db
from datetime import datetime

bp = Blueprint('account_routes', __name__)

@bp.route('/account')
@login_required
def account():
	return render_template('account.html', user=current_user)

@bp.route('/deposit', methods=['GET', 'POST'])
@login_required
def deposit():
	if request.method == 'POST':
		amount = float(request.form['amount'])
		if amount > 0:
			current_user.balance += amount
			txn = Transaction(amount=amount, type='deposit', timestamp=datetime.now(), user_id=current_user.id)
			db.session.add(txn)
			db.session.commit()
			flash('Deposit successful!')
			return redirect(url_for('account_routes.account'))
		else:
			flash('Enter a valid amount.')
	return render_template('transaction_form.html', action='Deposit')

@bp.route('/withdraw', methods=['GET', 'POST'])
@login_required
def withdraw():
	if request.method == 'POST':
		amount = float(request.form['amount'])
		if 0 < amount <= current_user.balance:
			current_user.balance -= amount
			txn = Transaction(amount=amount, type='withdraw', timestamp=datetime.now(), user_id=current_user.id)
			db.session.add(txn)
			db.session.commit()
			flash('Withdrawal successful!')
			return redirect(url_for('account_routes.account'))
		else:
			flash('Invalid amount or insufficient funds.')
	return render_template('transaction_form.html', action='Withdraw')

@bp.route('/transactions')
@login_required
def transactions():
	txns = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.timestamp.desc()).all()
	return render_template('transactions.html', transactions=txns)
