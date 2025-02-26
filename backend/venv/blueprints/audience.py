from flask import Blueprint, jsonify
import requests
import os
from tweepy import Client

bp = Blueprint('audience', __name__)

X_API_KEY = os.environ.get('X_API_KEY')
XAI_API_KEY = os.environ.get('XAI_API_KEY')
X_BEARER_TOKEN = os.environ.get('X_BEARER_TOKEN')

@bp.route('/audience/analyze')
def analyze_audience():
   client = Client(bearer_token= X_BEARER_TOKEN)


user_id = 'user_id'

# Get followers with additional user fields like location for more detailed analysis
followers = client.get_users_followers(id=user_id_or_username, max_results=100, user_fields=['location', 'description'], expansions=['pinned_tweet_id'])

# Iterate through the followers to gather information
for follower in followers.data:
    print(f"Follower: {follower.username}, Location: {follower.location}, Description: {follower.description}") 
    


