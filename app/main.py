from flask import Flask
from flask_marshmallow import Marshmallow 
from views.student import student_bp 
from views.subject import subject_bp 
from views.academic import academic_bp
from views.teacher import teacher_bp


ma = Marshmallow()
app = Flask(__name__)
ma.init_app(app)


app.register_blueprint(student_bp)
app.register_blueprint(subject_bp)
app.register_blueprint(academic_bp)
app.register_blueprint(teacher_bp)


if __name__ == "__main__":
    app.run(debug=True)










