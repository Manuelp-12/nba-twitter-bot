import tweepy
import csv
import random
import time
from tweepy.errors import TooManyRequests
from credentials import *

players = [] #array of all players

with open('nbaplayerlist.csv', mode='r', newline='', encoding='utf-8') as file: #goes through each row in csv
    reader = csv.reader(file)

    for row in reader:
        cleaned_row = [cell.rstrip() for cell in row] #removes extra spaces
        players.append(cleaned_row) #adds to array

client = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=access_token_secret)

while (len(players) > 0):
    random_player = random.choice(players) #chooses random player

    try:
        client.create_tweet(text=random_player[0]) #converts array element to string
        print("Player printed and removed.")
        players.remove(random_player) #removes random player

        #rewrite csv file with new list
        with open('nbaplayerlist.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(players)

        time.sleep(85 * 60) #runs every 85 mins (17 tweets a day)
    except TooManyRequests as e:
        print("Hit rate limit.")
        time.sleep(10 * 60) # sleep for 10 min