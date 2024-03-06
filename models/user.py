#define the database schema for users: 
# from werkzeug.security import generate_password_hash, check_password_hash
from app import db  

# methods for setting and checking passwords. 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # # hashes a plaintext password and saves the hash
    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password, method='bcrypt')

    # # verifies a plaintext password against the stored hash
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,  
        }