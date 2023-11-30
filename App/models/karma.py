from App.database import db
from .student import Student
from .KarmaStrategy import KarmaStrategy


class Karma(db.Model):
  __tablename__ = "karma"
  karmaID = db.Column(db.Integer, primary_key=True)
  score = db.Column(db.Float, nullable=False, default=0.0)
  rank = db.Column(db.Integer, nullable=False, default=-99)

  def __init__(self, strategy: KarmaStrategy, score=0.0, rank=-99):
    self.strategy = strategy
    self.score = score
    self.rank = rank

  def to_json(self):
    return {"karmaID": self.karmaID, "score": self.score, "rank": self.rank}

  def set_strategy(self, strategy: KarmaStrategy):
        self.strategy = strategy

  def execute_strategy(self, student):
      self.strategy.execute(student)


  """ @classmethod
  def getScore(cls, karmaID):
    # Retrieve the karma score by karma id
    karma = cls.query.filter_by(karmaID=karmaID).first()
    if karma:
      return karma.score
    return None  """
