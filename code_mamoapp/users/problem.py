from users import db

class Problem(db.Model):
    __tablename__='problems_data'

    id=db.Column(db.Integer,primary_key=True)
    language=db.Column(db.String(20))
    error_name=db.Column(db.String(64))
    error_content=db.Column(db.String(2000))

    def __init__(self,language,error_name,error_content):
        self.language=language
        self.error_name=error_name
        self.error_content=error_content

    def __repr__(self):
        return f"language:{self.language}"

