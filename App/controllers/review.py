from App.models import Review, Karma, Student, CalculateScoreStrategy
from App.database import db

def get_reviews(): 
    return db.session.query(Review).all()

def get_reviews_for_student(studentID):
    return db.session.query(Review).filter_by(studentID=studentID).all()

def get_review(reviewID):
    return Review.query.filter_by(ID=reviewID).first()

def get_reviews_by_staff(staffID):
    return db.session.query(Review).filter_by(reviewerID=staffID).all()


def edit_review(review, staff, is_positive, comment):
    if review.reviewer == staff:
        review.isPositive = is_positive
        review.comment = comment
        db.session.add(review)
        db.session.commit()
        return review
    return None


def delete_review(review, staff):
    if review.reviewer == staff:
        db.session.delete(review)
        db.session.commit()
        return True
    return None


def downvoteReview(reviewID, staff):
    review = db.session.query(Review).get(reviewID)
    strategy = CalculateScoreStrategy()  # or UpdateRankStrategy(), depending on your requirements


    if staff in review.staffDownvoters:  # If they downvoted the review already, return current votes
        return review.downvotes

    else:
        if staff not in review.staffDownvoters:  # if staff has not downvoted allow the vote
            review.downvotes += 1
            review.staffDownvoters.append(staff)

            if staff in review.staffUpvoters:  # if they had upvoted previously then remove their upvote to account for switching between votes
                review.upvotes -= 1
                review.staffUpvoters.remove(staff)

        db.session.add(review)
        db.session.commit()
        # Retrieve the associated Student object using studentID
        student = db.session.query(Student).get(review.studentID)

        # Check if the student has a Karma record (karmaID) and create a new Karma record for them if not
        if student.karmaID is None:
            karma = Karma(strategy, score=0.0, rank=-99)
            db.session.add(karma)  # Add the Karma record to the session
            db.session.flush()  # Ensure the Karma record gets an ID
            db.session.commit()
            # Set the student's karmaID to the new Karma record's ID
            student.karmaID = karma.karmaID

        student_karma = db.session.query(Karma).get(student.karmaID)
        student_karma.set_strategy(strategy)
        student_karma.execute_strategy(student)


    return review.downvotes


def upvoteReview(reviewID, staff):
    review = db.session.query(Review).get(reviewID)
    #if review is None:
        #raise ValueError("Invalid reviewID")

    strategy = CalculateScoreStrategy() # Define strategy here

    if staff not in review.staffUpvoters: 
        review.upvotes += 1
        review.staffUpvoters.append(staff)

        if staff in review.staffDownvoters: 
            review.downvotes -= 1
            review.staffDownvoters.remove(staff)

    db.session.add(review)
    db.session.commit()
    student = db.session.query(Student).get(review.studentID)

    if student.karmaID is None:
        karma = Karma(strategy=strategy, score=0.0, rank=-99) # Ensure strategy is passed as an argument
        db.session.add(karma)
        db.session.flush()

        student.karmaID = karma.karmaID

    student_karma = db.session.query(Karma).get(student.karmaID)
    student_karma.set_strategy(strategy)
    student_karma.execute_strategy(student)

    db.session.commit()

    return review.upvotes
