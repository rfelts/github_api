#!/usr/bin/env python3

# Russell Felts
# Git Hub Api Activity 06

import sys
import json

import requests

if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(response.content)

    print("User {}'s last GitHub activity was at {}".format(username, events[0]['created_at']))
