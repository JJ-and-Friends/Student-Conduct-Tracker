from App.models import Staff, Student, Admin, User
from App.database import db


def create_student(firstname, lastname, password, studentID, contact, studentType, yearofStudy):
    new_student = Student(firstname=firstname, lastname=lastname, password=password,
                          studentID=studentID, contact=contact, studentType=studentType, yearofStudy=yearofStudy)
    db.session.add(new_student)
    db.session.commit()
    return new_student


def create_staff(firstname, lastname, password, staffID, email, teachingExperience):
    new_staff = Staff(firstname=firstname, lastname=lastname, password=password,
                      staffID=staffID, email=email, teachingExperience=teachingExperience)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff


def create_user(firstname, password):
    new_admin = Admin(firstname=firstname, lastname='bobbing', password=password)
    db.session.add(new_admin)
    db.session.commit()
    return new_admin


def get_staff(staffID):
    return db.session.query(Staff).get(staffID)


def get_student(studentID):
    return db.session.query(Student).get(studentID)


def is_staff(staffID):
    return db.session.query(Staff).get(staffID) is not None


def is_student(studentID):
    return db.session.query(Student).get(studentID) is not None


def is_admin(AdminID):
    return db.session.query(Admin).get(AdminID) is not None 

def get_all_users_json():
    users = get_all_users()
    if not users:
        return []
    users = [user.to_json() for user in users]
    return users

def get_all_students_json():
    students = get_all_students()
    if not students:
        return []
    students = [student.to_json() for student in students]
    return students


def get_all_staff_json():
    staff_members = get_all_staff()
    if not staff_members:
        return []
    staff_members = [staff.to_json() for staff in staff_members]
    return staff_members

def get_all_users():
    return db.session.query(Admin).all() +  db.session.query(Staff).all() + db.session.query(Student).all()

def get_all_students():
    return db.session.query(Student).all()

def get_all_staff():
    return db.session.query(Staff).all()


def update_student(student, contacts, student_type, yearofStudy):
    student.contact = contacts
    student.studentType = student_type
    student.yearOfStudy = yearofStudy
    db.session.add(student)
    db.session.commit()
    return student
    
