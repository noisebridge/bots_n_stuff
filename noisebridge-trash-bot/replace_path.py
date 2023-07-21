import os
import argparse

CRON_FILE="trash_cron"
PYTHON_FILE="remind_trash"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uri", help="Discord Webhook uri")
    return parser.parse_args()

def replace_in_file(filename, ext, original, replacement):
    text=""
    with open(filename + "_template" + ext, "r") as f:
        text = f.read()
    text = text.replace(original, replacement) 
    with open(filename + ext, "w") as f:
        f.write(text)

def test_discord_uri():
    # Test posting
    from remind_trash import WEBHOOK_URI
    import requests
    import json
    result = requests.post(WEBHOOK_URI, json=json.load(open('test.json')))
    print("This should've posted to Discord!")

if __name__ == "__main__":
    currdir=os.path.dirname(os.path.realpath(__file__))
    args = parse_args()
    replace_in_file(os.path.join(currdir, CRON_FILE), "", "{PATH}", currdir)
    replace_in_file(os.path.join(currdir, PYTHON_FILE), ".py", "{URI}", args.uri)
    test_discord_uri()

