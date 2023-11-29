from .student import Student
from App.database import db
from .KarmaStrategy import KarmaStrategy

class CalculateScoreStrategy(KarmaStrategy):
    def execute(self, student):
        goodKarma = 0
        badKarma = 0

        # Iterate through reviews associated with the student
        for review in student.reviews:
            if review.isPositive == True:
                goodKarma += review.upvotes
                badKarma += review.downvotes
            else:
                badKarma += review.upvotes
                goodKarma += review.downvotes
        return (goodKarma - badKarma) / len(student.reviews)