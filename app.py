from flask import Flask, request, jsonify
import sqlite3
from database import create_tables, get_connection

app = Flask(__name__)

# Create database tables
create_tables()


@app.route("/")
def home():
    return jsonify({
        "message": "Sports Event Management REST API",
        "status": "Running Successfully"
    })


# GET - View all events
@app.route("/events", methods=["GET"])
def get_events():
    conn = get_connection()
    events = conn.execute("SELECT * FROM events").fetchall()
    conn.close()

    return jsonify([dict(event) for event in events]), 200


# POST - Create a new event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    required_fields = ["event_name", "sport", "venue", "event_date"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field} is required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO events (event_name, sport, venue, event_date)
        VALUES (?, ?, ?, ?)
    """, (
        data["event_name"],
        data["sport"],
        data["venue"],
        data["event_date"]
    ))

    event_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return jsonify({
        "message": "Event created successfully",
        "event_id": event_id
    }), 201


# GET - View event by ID
@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    conn = get_connection()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    conn.close()

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    return jsonify(dict(event)), 200


# PUT - Update event
@app.route("/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    conn = get_connection()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    if event is None:
        conn.close()
        return jsonify({"error": "Event not found"}), 404

    event_name = data.get("event_name", event["event_name"])
    sport = data.get("sport", event["sport"])
    venue = data.get("venue", event["venue"])
    event_date = data.get("event_date", event["event_date"])
    status = data.get("status", event["status"])

    conn.execute("""
        UPDATE events
        SET event_name = ?,
            sport = ?,
            venue = ?,
            event_date = ?,
            status = ?
        WHERE id = ?
    """, (event_name, sport, venue, event_date, status, event_id))

    conn.commit()
    conn.close()

    return jsonify({"message": "Event updated successfully"}), 200


# DELETE - Delete event
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    conn = get_connection()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    if event is None:
        conn.close()
        return jsonify({"error": "Event not found"}), 404

    conn.execute("DELETE FROM events WHERE id = ?", (event_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Event deleted successfully"}), 200
# GET - View all teams
@app.route("/teams", methods=["GET"])
def get_teams():
    conn = get_connection()

    teams = conn.execute("""
        SELECT teams.*, events.event_name
        FROM teams
        LEFT JOIN events ON teams.event_id = events.id
    """).fetchall()

    conn.close()

    return jsonify([dict(team) for team in teams]), 200


# POST - Register a new team
@app.route("/teams", methods=["POST"])
def register_team():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    required_fields = ["team_name", "captain", "event_id"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    conn = get_connection()

    # Check whether event exists
    event = conn.execute(
        "SELECT id FROM events WHERE id = ?",
        (data["event_id"],)
    ).fetchone()

    if event is None:
        conn.close()
        return jsonify({"error": "Event not found"}), 404

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO teams (team_name, captain, event_id)
        VALUES (?, ?, ?)
    """, (
        data["team_name"],
        data["captain"],
        data["event_id"]
    ))

    team_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Team registered successfully",
        "team_id": team_id
    }), 201
# GET - View all players
@app.route("/players", methods=["GET"])
def get_players():
    conn = get_connection()

    players = conn.execute("""
        SELECT players.*, teams.team_name
        FROM players
        LEFT JOIN teams ON players.team_id = teams.id
    """).fetchall()

    conn.close()

    return jsonify([dict(player) for player in players]), 200


# POST - Register a player
@app.route("/players", methods=["POST"])
def register_player():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    required_fields = ["player_name", "age", "team_id"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    conn = get_connection()

    # Check team exists
    team = conn.execute(
        "SELECT id FROM teams WHERE id = ?",
        (data["team_id"],)
    ).fetchone()

    if team is None:
        conn.close()
        return jsonify({"error": "Team not found"}), 404

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO players (player_name, age, team_id)
        VALUES (?, ?, ?)
    """, (
        data["player_name"],
        data["age"],
        data["team_id"]
    ))

    player_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Player registered successfully",
        "player_id": player_id
    }), 201

# GET - View all matches
@app.route("/matches", methods=["GET"])
def get_matches():
    conn = get_connection()

    matches = conn.execute("""
        SELECT 
            matches.*,
            t1.team_name AS team1_name,
            t2.team_name AS team2_name,
            events.event_name
        FROM matches
        LEFT JOIN teams t1 ON matches.team1_id = t1.id
        LEFT JOIN teams t2 ON matches.team2_id = t2.id
        LEFT JOIN events ON matches.event_id = events.id
    """).fetchall()

    conn.close()

    return jsonify([dict(match) for match in matches]), 200


# POST - Schedule a new match
@app.route("/matches", methods=["POST"])
def schedule_match():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    required_fields = [
        "event_id",
        "team1_id",
        "team2_id",
        "match_date"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    if data["team1_id"] == data["team2_id"]:
        return jsonify({
            "error": "A team cannot play against itself"
        }), 400

    conn = get_connection()

    # Check event exists
    event = conn.execute(
        "SELECT id FROM events WHERE id = ?",
        (data["event_id"],)
    ).fetchone()

    if event is None:
        conn.close()
        return jsonify({"error": "Event not found"}), 404

    # Check both teams exist
    team1 = conn.execute(
        "SELECT id FROM teams WHERE id = ?",
        (data["team1_id"],)
    ).fetchone()

    team2 = conn.execute(
        "SELECT id FROM teams WHERE id = ?",
        (data["team2_id"],)
    ).fetchone()

    if team1 is None or team2 is None:
        conn.close()
        return jsonify({"error": "Team not found"}), 404

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO matches (
            event_id,
            team1_id,
            team2_id,
            match_date
        )
        VALUES (?, ?, ?, ?)
    """, (
        data["event_id"],
        data["team1_id"],
        data["team2_id"],
        data["match_date"]
    ))

    match_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Match scheduled successfully",
        "match_id": match_id
    }), 201

# PUT - Update match score and declare winner
@app.route("/matches/<int:match_id>/score", methods=["PUT"])
def update_score(match_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    if "score1" not in data or "score2" not in data:
        return jsonify({
            "error": "Both scores are required"
        }), 400

    score1 = data["score1"]
    score2 = data["score2"]

    if (not isinstance(score1, int) or isinstance(score1, bool)
            or not isinstance(score2, int) or isinstance(score2, bool)):
        return jsonify({
            "error": "Scores must be integers"
        }), 400

    if score1 < 0 or score2 < 0:
        return jsonify({
            "error": "Scores cannot be negative"
        }), 400

    conn = get_connection()

    match = conn.execute(
        "SELECT * FROM matches WHERE id = ?",
        (match_id,)
    ).fetchone()

    if match is None:
        conn.close()
        return jsonify({"error": "Match not found"}), 404

    if score1 > score2:
        winner = match["team1_id"]
    elif score2 > score1:
        winner = match["team2_id"]
    else:
        winner = "Draw"

    if winner != "Draw":
        winner_team = conn.execute(
            "SELECT team_name FROM teams WHERE id = ?",
            (winner,)
        ).fetchone()

        winner = winner_team["team_name"]

    conn.execute("""
        UPDATE matches
        SET score1 = ?,
            score2 = ?,
            winner = ?,
            status = 'Completed'
        WHERE id = ?
    """, (score1, score2, winner, match_id))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Score updated successfully",
        "match_id": match_id,
        "score1": score1,
        "score2": score2,
        "winner": winner,
        "status": "Completed"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)