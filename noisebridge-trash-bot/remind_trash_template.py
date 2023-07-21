from datetime import date, datetime
import json
import requests
import os

WEBHOOK_URI="{URI}"
CONTENT_FILENAME="remind.json"

if __name__=="__main__":
    content_path=os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            CONTENT_FILENAME
            )
    content=json.load(open(content_path))
    result = requests.post(WEBHOOK_URI, json=content)

