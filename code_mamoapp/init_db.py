from users import db
from users.problem import Problem

db.drop_all()
db.create_all()

problems1=Problem(language="html1",error_name="1",error_content="error1")
db.session.add(problems1) 
problems1=Problem(language="html2",error_name="2",error_content="error2")
db.session.add(problems1) 
problems1=Problem(language="html3",error_name="3",error_content="error3")
db.session.add(problems1) 
problems1=Problem(language="html4",error_name="4",error_content="error4")
db.session.add(problems1) 
problems1=Problem(language="html5",error_name="5",error_content="error5")
db.session.add(problems1) 
problems1=Problem(language="html6",error_name="6",error_content="error6")
db.session.add(problems1) 
problems1=Problem(language="html7",error_name="7",error_content="error7")
db.session.add(problems1) 
problems1=Problem(language="html8",error_name="8",error_content="error8")
db.session.add(problems1) 
problems1=Problem(language="html9",error_name="9",error_content="error9")
db.session.add(problems1) 
problems1=Problem(language="html10",error_name="10",error_content="error10")
db.session.add(problems1) 

db.session.commit()