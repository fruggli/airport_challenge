# Airport Challenge 
This repository provides a REST API that find the closest airport for a list of 100,000 users and its corresponding Wikipedia page for a given user ID.

## Files Included

- **airports_filter.py**: Script to create `airports_w_wiki.csv`.
- **airports_w_wiki.csv**: CSV file containing airport data with Wikipedia links.
- **app.py**: Main application file that runs the REST API.
- **create_closest_airport.py**: Script to create `user_closest_airport.csv`.
- **requirements.txt**: List of dependencies required to run the application.
- **user_closest_airport.csv**: CSV file containing user-specific nearest airport data.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/nearest-airports-api.git
   cd nearest-airports-api
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
 3. **Install the required dependencies:**
    ```bash
     pip install -r requirements.txt
     ```
4. **Optional: Generate the necessary CSV files:**
   ```bash
   python airports_filter.py #to create airports_w_wiki.csv
   python create_closest_airport.py #to create user_closest_airport.csv
   ```
5. **Run the application:**
   ```bash
    python app.py
   ```

## API Endpoints

The API provides the following endpoints to retrieve data:

```python
import requests

BASE_PATH = 'http://localhost:5000'
user_id = 'example_user_id'
response = requests.get(f"{BASE_PATH}/nearest_airports/{user_id}")
airport_id = response.json()["airport_id"]

response = requests.get(f"{BASE_PATH}/nearest_airports_wikipedia/{user_id}")
wikipedia_page = response.json()["wikipedia_page"]

```
