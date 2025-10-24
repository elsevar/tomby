from django.shortcuts import render
from slack import WebClient
from slack_sdk.errors import SlackApiError
import os
import json
from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

# Create your views here.
client = WebClient(token=os.environ["SLACK_KEY"])

def get_user_id_by_email(email: str) -> str | None:
    try:
        res = client.users_lookupByEmail(email=email)  # needs users:read.email
        return res["user"]["id"]
    except SlackApiError as e:
        print(f"Lookup failed: {e.response}")
        return None
    
def dm_user_by_id(user_id: str, text: str):
    try:
        # 1) Open (or fetch) a DM with the user
        opened = client.conversations_open(users=[user_id])  # note: 'users' (plural)
        dm_channel = opened["channel"]["id"]

        # 2) Send the message to that DM channel
        client.chat_postMessage(channel=dm_channel, text=text)
        print("Message sent!")
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")


@csrf_exempt 
def gitlab_webhook_for_reviews(request: HttpRequest):
    payload = json.loads(request.body.decode('utf-8'))
    slack_user_id = get_user_id_by_email("elsever1@live.com")
    print(payload)
    dm_user_by_id(slack_user_id, payload)
    return JsonResponse(payload)