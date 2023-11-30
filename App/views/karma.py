from flask import Blueprint, jsonify
from App.models import Karma, Student, UpdateRankStrategy
from App.database import db

# Create a Blueprint for karma views
karma_views = Blueprint("karma_views", __name__, template_folder='../templates')

# Route to update Karma rankings for all students
@karma_views.route("/karma/update_rankings", methods=["POST"])
def update_karma_rankings_route():
   # Retrieve all Karma instances from the database
   all_karma = Karma.query.all()

   # Create a new UpdateRankStrategy instance
   update_rank_strategy = UpdateRankStrategy()

   # Execute the strategy for each Karma instance
   for karma in all_karma:
       karma.execute_strategy(update_rank_strategy)

   # Commit the changes to the database
   db.session.commit()

   return "Karma rankings updated", 200
