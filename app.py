from flask import Flask, render_template, request, jsonify

import json
import random
import datetime

import classify_intent

app = Flask(__name__)

seat_count = 50

with open("dataset.json") as file:
    data = json.load(file)


@app.route('/')
def index():
    return render_template('index.html')


# def read_menu():


@app.route('/get')
def get_bot_response():
    global seat_count
    message = request.args.get('msg')

    if message:
        '''
        tag = classify_intent.classify(message)
        if len(tag) != 0:
            if tag == "book_table":
                seat_count -= 1
                response = "Your table has been booked successfully. Remaining tables: " + str(seat_count)

            elif tag == "available_tables":
                response = "There are " + str(seat_count) + " tables available at the moment."

            elif tag == "suggest":
                day = datetime.datetime.now()
                day = day.strftime("%A")
                if day == "Monday":
                    response = "Chef recommends: Steamed Tofu with Schezwan Peppercorn, Eggplant with Hot Garlic Sauce, Chicken & Chives, Schezwan Style, Diced Chicken with Dry Red Chilli, Schezwan Pepper"

                elif day == "Tuesday":
                    response = "Chef recommends: Asparagus Fresh Shitake & King Oyster Mushroom, Stir Fried Chilli Lotus Stem, Crispy Fried Chicken with Dry Red Pepper, Osmanthus Honey, Hunan Style Chicken"

                elif day == "Wednesday":
                    response = "Chef recommends: Baby Pokchoi Fresh Shitake Shimeji Straw & Button Mushroom, Mock Meat in Hot Sweet Bean Sauce, Diced Chicken with Bell Peppers & Onions in Hot Garlic Sauce, Chicken in Chilli Black Bean & Soy Sauce"

                elif day == "Thursday":
                    response = "Chef recommends: Eggplant & Tofu with Chilli Oyster Sauce, Corn, Asparagus Shitake & Snow Peas in Hot Bean Sauce, Diced Chicken Plum Honey Chilli Sauce, Clay Pot Chicken with Dried Bean Curd Sheet"

                elif day == "Friday":
                    response = "Chef recommends: Kailan in Ginger Wine Sauce, Tofu with Fresh Shitake & Shimeji, Supreme Soy Sauce, Diced Chicken in Black Pepper Sauce, Sliced Chicken in Spicy Mala Sauce"

                elif day == "Saturday":
                    response = "Chef recommends: Kung Pao Potato, Okra in Hot Bean Sauce, Chicken in Chilli Black Bean & Soy Sauce, Hunan Style Chicken"

                elif day == "Sunday":
                    response = "Chef recommends: Stir Fried Bean Sprouts & Tofu with Chives, Vegetable Thou Sou, Diced Chicken Plum Honey Chilli Sauce, Diced Chicken in Black Pepper Sauce"
            else:
                for tg in data['intents']:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                response = random.choice(responses)
        else:
            response = "I didn't quite get that, please try again."
        '''
        response = "DUMMY_RESPONSE"

        return str(response)
    return "Missing Data!"


if __name__ == "__main__":
    app.run()
