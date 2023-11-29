from flask import Blueprint, jsonify
from App.database import db
from App.models import Karma, Student, UpdateRankStrategy
from App.controllers import Student

from App.controllers.karma import (
    update_student_karma_rankings,
)

# Create a Blueprint for karma views
karma_views = Blueprint("karma_views", __name__, template_folder='../templates')

# Route to update Karma rankings for all students
@karma_views.route("/karma/update_rankings", methods=["POST"])
def update_karma_rankings_route():
    update_rank_strategy = UpdateRankStrategy()
    update_rank_strategy.execute()
    return "Karma rankings updated", 200

"""
# Route to update Karma rankings for all students
@karma_views.route("/karma/update_rankings", methods=["POST"])
def update_karma_rankings_route():
    update_student_karma_rankings()
    return "Karma rankings updated", 200"""
