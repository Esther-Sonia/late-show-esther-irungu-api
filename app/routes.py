from flask import request, jsonify
from . import db
from .models import Episode, Guest, Appearance

def register_routes(app):

    @app.route('/episodes', methods=['GET'])
    def get_episodes():
        eps = Episode.query.all()
        return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in eps]), 200

    @app.route('/episodes/<int:id>', methods=['GET'])
    def get_episode(id):
        e = Episode.query.get(id)
        if not e:
            return jsonify({"error": "Episode not found"}), 404
        return jsonify(e.to_dict()), 200

    @app.route('/guests', methods=['GET'])
    def get_guests():
        gs = Guest.query.all()
        return jsonify([g.to_dict() for g in gs]), 200

    @app.route('/appearances', methods=['POST'])
    def create_appearance():
        data = request.get_json()
        try:
            app_obj = Appearance(
                rating=data['rating'],
                guest_id=data['guest_id'],
                episode_id=data['episode_id']
            )
            db.session.add(app_obj)
            db.session.commit()
            return jsonify(app_obj.to_dict()), 201
        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400
