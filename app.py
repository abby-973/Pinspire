from urllib.parse import unquote
from flask import Flask, jsonify, render_template, redirect, url_for, request
import sqlite3
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

'''@app.route('/api/cards', methods=['GET'])
def get_all_cards():
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM Cards")
        cards = cursor.fetchall()
        conn.close()

        # If the query returns no results, ensure cards is an empty list
        if not cards:
            cards = []

        # Convert the results into a list of dictionaries
        card_list = []
        for card in cards:
            if card:  # Ensure card is not None
                card_dict = {
                    'cardId': card[0],
                    'name': card[1],
                    'description': card[2],
                    'type': card[3],
                    'imgURL': unquote(card[4]) if card[4] else ''  # Decode imgUrl if it exists
                }
                card_list.append(card_dict)

        # Log for debugging
        print({'cards': card_list})

        # Return the JSON response
        return jsonify({'cards': card_list})

    except Exception as e:
        # Log the error for debugging
        print(f"Error fetching cards: {str(e)}")
        return jsonify({'error': str(e)}) '''
