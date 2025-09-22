from flask import Flask
import os
from extensions import db, login_manager
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


from flask import redirect, url_for
from routes import auth_routes, account_routes
app.register_blueprint(auth_routes.bp)
app.register_blueprint(account_routes.bp)

# Redirect root URL to login
@app.route('/')
def home():
    return redirect(url_for('auth_routes.login'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
