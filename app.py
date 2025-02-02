from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DATABASE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Group(db.Model):
    __tablename__ = 'groups'
    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100), nullable=False, unique=True)


class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))


class Teacher(db.Model):
    __tablename__ = 'teachers'
    teacher_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)


class Subject(db.Model):
    __tablename__ = 'subjects'
    subject_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(100), nullable=False, unique=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'))


class Attendance(db.Model):
    __tablename__ = 'attendance'
    attendance_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    date_presence = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)


class Grade(db.Model):
    __tablename__ = 'grades'
    grade_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    date_grade = db.Column(db.Date, nullable=False)
    grade = db.Column(db.Integer, nullable=False)


class Assignment(db.Model):
    __tablename__ = 'assignments'
    assignment_id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    title = db.Column(db.String(100), nullable=False)
    descriptions = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=False)


@app.route('/api/groups', methods=['GET', 'POST'])
def handle_groups():
    if request.method == 'GET':
        groups = Group.query.all()
        return jsonify([{'id': group.group_id, 'group_name': group.group_name} for group in groups]), 200
    if request.method == 'POST':
        data = request.get_json()
        new_group = Group(group_name=data['group_name'])
        db.session.add(new_group)
        db.session.commit()
        return jsonify({'id': new_group.group_id, 'group_name': new_group.group_name}), 201



@app.route('/api/students', methods=['GET', 'POST'])
def handle_students():
    if request.method == 'GET':
        students = Student.query.all()
        return jsonify([{'id': student.student_id, 'first_name': student.first_name, 'last_name': student.last_name, 'middle_name': student.middle_name} for student in students]), 200
    if request.method == 'POST':
        data = request.get_json()
        new_student = Student(first_name=data['first_name'], last_name=data['last_name'], middle_name=data['middle_name'], group_id=data['group_id'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'id': new_student.id, 'first_name': new_student.first_name, 'last_name': new_student.last_name}), 201



if __name__ == '__main__':
    app.run(debug=True)
