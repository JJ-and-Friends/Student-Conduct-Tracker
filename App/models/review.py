from App.database import db
from .student import Student
from datetime import datetime
from .karma import Karma
from abc import ABC, abstractmethod

# Define the association table for staff upvotes on reviews
review_staff_upvoters = db.Table(
    'review_staff_upvoters',
    db.Column('reviewID', db.Integer, db.ForeignKey('review.ID')),
    db.Column('staffID', db.String(10), db.ForeignKey('staff.ID')),
)

review_staff_downvoters = db.Table(
    'review_staff_downvoters',
    db.Column('reviewID', db.Integer, db.ForeignKey('review.ID')),
    db.Column('staffID', db.String(10), db.ForeignKey('staff.ID')),
)


class Review(db.Model):
  __tablename__ = 'review'
  ID = db.Column(db.Integer, primary_key=True)
  reviewerID = db.Column(
      db.String(10),
      db.ForeignKey('staff.ID'))  #each review has 1 creator

  #create reverse relationship from Staff back to Review to access reviews created by a specific staff member
  reviewer = db.relationship('Staff',
                             backref=db.backref('reviews_created',
                                                lazy='joined'),
                             foreign_keys=[reviewerID])

  studentID = db.Column(db.String(10), db.ForeignKey('student.ID'))

  staffUpvoters = db.relationship(
      'Staff',
      secondary=review_staff_upvoters,
      backref=db.backref(
          'reviews_upvoted',
          lazy='joined'))  #for staff who have voted on the review

  staffDownvoters = db.relationship(
      'Staff',
      secondary=review_staff_downvoters,
      backref=db.backref(
          'reviews_downvoted',
          lazy='joined'))  #for staff who have voted on the review

  upvotes = db.Column(db.Integer, nullable=False)
  downvotes = db.Column(db.Integer, nullable=False)
  created = db.Column(db.DateTime, default=datetime.utcnow)
  comment = db.Column(db.String(400), nullable=False)

 
  @abstractmethod
  def __init__(self, reviewer, student, comment):
    pass
 
  @abstractmethod
  def get_id(self):
    pass


  @abstractmethod
  def editReview(self, staff, comment):
    pass

 
  @abstractmethod
  def deleteReview(self, staff):
    pass

  
  @abstractmethod
  def upvoteReview(self, staff): 
    pass

    
  @abstractmethod
  def downvoteReview(self, staff): 
    pass

  @abstractmethod
  def to_json(self):
    pass
