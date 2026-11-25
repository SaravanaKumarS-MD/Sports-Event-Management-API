# Sports Event Management REST API

## Project Overview
Sports Event Management REST API is a backend application developed using Python Flask and SQLite. It helps manage sports events, teams, players, matches, scores, and winners through REST API endpoints.

## Objectives
- Manage sports events.
- Register teams and players.
- Schedule matches.
- Update match scores.
- Automatically determine match winners.
- Handle invalid inputs and errors.

## Technologies Used
- Python
- Flask
- SQLite
- REST API
- JSON
- urllib

## Modules
1. Event Management
2. Team Registration
3. Player Management
4. Match Scheduling
5. Score Management
6. Winner Calculation
7. Error Handling

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/events` | View all events |
| POST | `/events` | Create event |
| GET | `/events/<id>` | View specific event |
| PUT | `/events/<id>` | Update event |
| DELETE | `/events/<id>` | Delete event |
| GET | `/teams` | View teams |
| POST | `/teams` | Register team |
| GET | `/players` | View players |
| POST | `/players` | Register player |
| GET | `/matches` | View matches |
| POST | `/matches` | Schedule match |
| PUT | `/matches/<id>/score` | Update score and winner |

## Database
SQLite database contains four tables:

- Events
- Teams
- Players
- Matches

## Testing
The application was tested using Python testing scripts.

Test cases include:
- Event creation and retrieval
- Team registration
- Player registration
- Match scheduling
- Score updating
- Winner calculation
- Invalid event ID
- Invalid team ID
- Negative score
- Missing required fields

All test cases were successfully completed.

## Result
The Sports Event Management REST API was successfully developed using Flask and SQLite. The application supports event management, team and player registration, match scheduling, score updates, winner calculation, and error handling.