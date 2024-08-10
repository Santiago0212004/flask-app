from app import app, db
from models import Team

with app.app_context():
    db.create_all()
    teams = ['Team A', 'Team B', 'Team C']
    for team_name in teams:
        team = Team(name=team_name)
        db.session.add(team)
    db.session.commit()