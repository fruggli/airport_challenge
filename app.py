from flask import Flask, redirect, request, jsonify, render_template, url_for, abort
import pandas as pd


app = Flask(__name__)

# Load the data
user = pd.read_csv('user_closest_airport.csv')  
airports = pd.read_csv('airports_w_wiki.csv')
# Merge the DataFrames on the airport_id and id columns
merged_data = pd.merge(user, airports[['id', 'wikipedia_link']], left_on='airport_id', right_on='id', how='left')

# Drop the 'id' column from the merged DataFrame
merged_data.drop(columns=['id'], inplace=True)

# Convert the DataFrame to a dictionary for quick lookup
user_airport_dict = merged_data.set_index('user_id')[['airport_id', 'wikipedia_link']].to_dict('index')

@app.route('/')
def home():
    return "Welcome to the Nearest Airport Finder!"

# creat endpoint for nearest airport
@app.route('/nearest_airports/<int:user_id>', methods=['GET'])
def get_nearest_airport(user_id):
    user_info = user_airport_dict.get(user_id)
    if user_info:
        return jsonify({'airport_id': user_info['airport_id']})
    else:
        abort(404, description="User ID not found")
   
# create endpoint for wikipedia page     
@app.route('/nearest_airports_wikipedia/<int:user_id>', methods=['GET'])
def get_nearest_airport_wiki(user_id):
    user_info = user_airport_dict.get(user_id)
    if user_info:
        return jsonify({'wikipedia_page': user_info['wikipedia_link']})
        #return jsonify({'wikipedia_link': user_info['wikipedia_link']})
    else:
        abort(404, description="User ID not found")


if __name__ == '__main__':
    app.run(debug=True)