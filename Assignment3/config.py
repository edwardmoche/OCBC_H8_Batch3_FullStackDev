import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
# # ini buat alamat lokasi db
# # kalo copas dari git isinya ini
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# # kalo di colab ini
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
# # ini buat connenct ke heroku
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hhjxjdwcyxbeka:d3c828a7cb98b11e0b4e47f7f854f3a6d35eb1bedc8a8bc744e15ca238cdf073@ec2-3-229-252-6.compute-1.amazonaws.com:5432/dahet4t7jk243h' + os.path.join(basedir, 'people.db')
uri = os.getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hhjxjdwcyxbeka:d3c828a7cb98b11e0b4e47f7f854f3a6d35eb1bedc8a8bc744e15ca238cdf073@ec2-3-229-252-6.compute-1.amazonaws.com:5432/dahet4t7jk243h'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)