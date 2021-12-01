import requests

req = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
req.raise_for_status()
req_json = req.json()
question_data = req_json['results']