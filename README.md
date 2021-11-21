# Restaurant-chatbot

Detailed explanation of the project is given in my tech blog here: https://medium.com/@barua.aindriya/building-a-nlp-chatbot-for-a-restaurant-with-flask-b978337049f2

How to set up and run the project?

1. Install Pre-requisites
My python version is 3.6.13.
To install all the required libraries, download/clone my GitHub repo and in the folder, open CMD and enter:  
> pip install -r requirements.txt

2. Download pre-trained FastText English model
Download cc.en.300.bin.gz from https://fasttext.cc/docs/en/crawl-vectors.html . Unizip it to Download cc.en.300.bin, the code for which is helper scripts in my Github repo.
3. Prepare dataset
Run data_embedder.py This will take the dataset.json file and convert all the sentences to FastText Vectors.
> python data_embedder.py
4. Set up Mongo Db on localhost
Install MongoDb Compass
Make 3 collections: menu, bookings, feedback
Menu has to be hardcoded, it includes item, cost, vegan, veg, about, offer.

feedback docs will be inserted when a user gives a feedback so that the restaurant authority can read them and take necessary action.

booking collection writer the unique booking ID and time-stamp of booking, so that when the customer comes and shows the ID at the reception, the booking can be verified.

5. Run Flask
This will launch the web app on localhost
> export FLASK_APP=app  
> export FLASK_ENV=development  
> flask run  
