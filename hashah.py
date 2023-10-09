db="DataLink"
class Video(db.Model):
    __tablename__ = "videos"
    id= db.Column(db.Integer,primary_key=True)   
    name= db.Column(db.String(200),nullable=False)
    video_link= db.Column(db.String,nullable=False)
    Likes= db.Column(db.Integer)
    Subs= db.Integer(db.Integer)
    
db="Login"
class Login(db.Model):
    __tablename__ = "Login"
    id= db.Column(db.Integer,primary_key=True)   
    name= db.Column(db.String(200),nullable=False)
    Password= db.Column(db.String(200), nullable=False)
    

db="Personal Details"
class Login(db.Model):
    __tablename__ = "Login"
    id= db.Column(db.Integer,primary_key=True) 
    DOB= db.Column(db.Integer(8),nullable=False) 
    Adress= db.Column(db.String(200),nullable=False) 
    
db="University Form"
class Form(db.Form)
   __tablename__ = "University Form"
   course= db.Column(db.Integer,primary_key=True)
   State_of_origin= db.Column(db.String(200), nullable=False)
