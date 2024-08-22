from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Initialize the database
db = SQLAlchemy(app)


# Define the database model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    university = db.Column(db.String(100), nullable=False)
    niveau_etude = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Registration {self.full_name}>'


# Create the database and tables
with app.app_context():
    db.create_all()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        full_name = request.form['full_name']
        email = request.form['email']
        university = request.form['university']
        niveau_etude = request.form['niveau_etude']

        # Check if the email already exists
        existing_user = Registration.query.filter_by(email=email).first()
        if existing_user:
            flash('This email is already registered. Please use a different email.')
            return redirect(url_for('register'))

        # Create a new registration record
        new_registration = Registration(
            full_name=full_name,
            email=email,
            university=university,
            niveau_etude=niveau_etude
        )

        # Add the record to the session and commit to the database
        try:
            db.session.add(new_registration)
            db.session.commit()
            return redirect(url_for('success'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while processing your registration. Please try again.')
            return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/success')
def success():
    return render_template("index.html")


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
