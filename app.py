from flask import Flask, render_template, request, jsonify

import json
import random
import datetime
import pymongo
import uuid

import classify_intent

app = Flask(__name__)

seat_count = 50

with open("dataset.json") as file:
    data = json.load(file)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["restaurant"]
menu_collection = db["menu"]
feedback_collection = db["feedback"]
bookings_collection = db["bookings"]


@app.route('/')
def index():
    return render_template('index.html')


def get_intent(message):
    tag = classify_intent.classify(message)
    return tag

def record_booking(booking_id):
    now = datetime.datetime.now()
    booking_time = now.strftime("%Y-%m-%d %H:%M:%S")
    booking_doc = {"booking_id": booking_id, "booking_time": booking_time}
    bookings_collection.insert_one(booking_doc)



def vegan_menu():
    query = {"vegan": "Y"}
    vegan_doc = menu_collection.find(query)
    response = "Vegan options are: "
    for x in vegan_doc:
        response = response + str(x.get("item")) + " for Rs. " + str(x.get("cost")) + "; "
    return response


def veg_menu():
    query = {"veg": "Y"}
    vegan_doc = menu_collection.find(query)
    response = "Vegetarian options are: "
    for x in vegan_doc:
        response = response + str(x.get("item")) + " for Rs. " + str(x.get("cost")) + "; "
    return response


def offers():
    all_offers = menu_collection.distinct('offer')
    response = "SPECIAL OFFERS: "
    for ofr in all_offers:
        docs = menu_collection.find({"offer": ofr})
        response = response + ofr.upper() + " On: "
        for x in docs:
            response = response + str(x.get("item")) + " - Rs. " + str(x.get("cost")) + "; "

    return response


def suggest():
    day = datetime.datetime.now()
    day = day.strftime("%A")
    if day == "Monday":
        response = "Chef recommends: Paneer Grilled Roll, Jade Chicken"
    elif day == "Tuesday":
        response = "Chef recommends: Tofu Cutlet, Chicken A La King"

    elif day == "Wednesday":
        response = "Chef recommends: Mexican Stuffed Bhetki Fish, Crispy corn"

    elif day == "Thursday":
        response = "Chef recommends: Mushroom Pepper Skewers, Chicken cheese balls"

    elif day == "Friday":
        response = "Chef recommends: Veggie Steak, White Sauce Veggie Extravaganza"

    elif day == "Saturday":
        response = "Chef recommends: Tofu Cutlet, Veggie Steak"

    elif day == "Sunday":
        response = "Chef recommends: Chicken Cheese Balls, Butter Garlic Jumbo Prawn"
    return response


def recipe_enquiry(message):
    all_foods = menu_collection.distinct('item')
    response = ""
    for food in all_foods:
        query = {"item": food}
        food_doc = menu_collection.find(query)[0]
        if food.lower() in message.lower():
            response = food_doc.get("about")
            break
    if "" == response:
        response = "Sorry please try again with exact spelling of the food item!"
    return response


def record_feedback(message, type):
    feedback_doc = {"feedback_string" : message, "type" : type}
    feedback_collection.insert_one(feedback_doc)


def get_specific_response(tag):
    for intent in data['intents']:
        if intent['tag'] == tag:
            responses = intent['responses']
    response = random.choice(responses)
    return response


@app.route('/get')
def get_bot_response():
    global seat_count
    message = request.args.get('msg')
    response = ""

    if message:
        tag = get_intent(message)
        if tag != "":
            if tag == "book_table":
                seat_count -= 1
                booking_id = uuid.uuid4()
                response = "Your table has been booked successfully. Please show this Booking ID at the counter: " + str(booking_id)

            elif tag == "available_tables":
                response = "There are " + str(seat_count) + " tables available at the moment."

            elif tag == "veg_enquiry":
                response = veg_menu()

            elif tag == "vegan_enquiry":
                response = vegan_menu()

            elif tag == "offers":
                response = offers()

            elif tag == "suggest":
                response = suggest()

            elif tag == "recipe_enquiry":
                response = recipe_enquiry(message)

            elif tag == "positive_feedback":
                record_feedback(message, "positive")
                response = get_specific_response(tag)

            elif "negative_response" == tag:
                record_feedback(message, "negative")
                response = get_specific_response(tag)

            else:
                response = get_specific_response(tag)

        else:
            response = "Sorry! I didn't quite get it, please try being more precise."
        return str(response)
    return "Missing Data!"


if __name__ == "__main__":
    app.run()
