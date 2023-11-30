from App.models import Karma, Student, KarmaStrategy
from App.database import db

def get_karma_by_id(karma_id):
    return db.session.query(Karma).get(karma_id)
    good_karma = 0
    bad_karma = 0

    for review in student.reviews:
        if review.isPositive:
            good_karma += review.upvotes
            bad_karma += review.downvotes
        else:
            bad_karma += review.upvotes
            good_karma += review.downvotes
        
        karma_score = good_karma - bad_karma

def calculate_student_karma(student):
    strategy = CalculateScoreStrategy()
    karma_score = strategy.execute(student)

    if student.karmaID is not None:
        karma = db.session.query(Karma).get(student.karmaID)
        karma.score = karma_score
    else:
        karma = Karma(strategy, score=karma_score)
        db.session.add(karma)
        db.session.flush() 
        student.karmaID = karma.karmaID

    db.session.commit()
    return karma

def update_student_karma_rankings():
    update_rank_strategy = UpdateRankStrategy()
    update_rank_strategy.execute()
