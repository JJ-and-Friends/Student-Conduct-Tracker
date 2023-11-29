from App.models.karma import Karma
from .student import Student
from App.database import db
from .KarmaStrategy import KarmaStrategy

class UpdateRankStrategy(KarmaStrategy):
    def execute(self):
        # Calculate the rank of students based on their karma score

        # Query all students with karma scores in descending order
        studentsOrdered = db.session.query(Student, Karma)\
                   .join(Karma, Student.karmaID == Karma.karmaID)\
                   .order_by(db.desc(Karma.score))\
                   .all()

        rank = 1
        prev_score = None

        #assign ranks to student with the highest karma at the top
        for student, karma in studentsOrdered:
            if prev_score is None:
                prev_score = karma.score
                karma.rank = rank
            elif prev_score == karma.score:
                karma.rank = rank
            else:
                rank += 1
                karma.rank = rank
                prev_score = karma.score

        # Commit the changes to the database
        db.session.commit()