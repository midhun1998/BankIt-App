from app import db
from app import Login

db.create_all()
print("***********************************")
print("Tables in DB are: "+ str(db.engine.table_names()))
# Login ID and Password for Logging In
# db.session.add(Login(uid=2, passw='password2'))
db.session.commit()
print("DB Created Successfully! \nUse ID: 2 and Password: password2 to Login as Employee.")
print("***********************************")