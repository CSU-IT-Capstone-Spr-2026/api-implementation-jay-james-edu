"""
XKCD Comic Viewer
"""
from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

XKCD_BASE_URL = "https://xkcd.com"
latest_comic_number = None

def get_latest_comic():
    # Fetch the most recent XKCD comic from the API
    global latest_comic_number
    try:
        response = requests.get(f"{XKCD_BASE_URL}/info.0.json")
        if response.status_code == 200:
            comic_data = response.json()
            latest_comic_number = comic_data['num']
            return comic_data
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


def get_comic_by_number(comic_num):
    # Fetch a specific XKCD comic by its number
    try:
        response = requests.get(f"{XKCD_BASE_URL}/{comic_num}/info.0.json")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Comic #{comic_num} not found")
            return None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


def get_latest_comic_number():
    # Helper function to get the latest comic number
    global latest_comic_number
    if latest_comic_number is None:
        latest = get_latest_comic()
        if latest:
            latest_comic_number = latest['num']
    return latest_comic_number


def get_recent_comics(count=5):
    # Fetch multiple recent comics (default 5)
    latest_num = get_latest_comic_number()
    if not latest_num:
        return []
    
    comics = []
    # Fetch the last 'count' comics
    for num in range(max(1, latest_num - count + 1), latest_num + 1):
        comic = get_comic_by_number(num)
        if comic:
            comics.append(comic)
    
    # Return in reverse chronological order (newest first)
    return list(reversed(comics))


@app.route('/')
def index():
    # Home page - displays the latest XKCD comic
    comic = get_latest_comic()
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None, 
                             error="Sorry, we couldn't fetch the comic right now. Please try again later.")


@app.route('/comic/<int:comic_num>')
def show_comic(comic_num):
    # Display a specific comic by number
    latest_num = get_latest_comic_number()
    
    if comic_num < 1:
        return render_template('index.html', comic=None,
                             error="Invalid comic number. Comics start at #1.")
    
    if latest_num and comic_num > latest_num:
        return render_template('index.html', comic=None,
                             error=f"Comic #{comic_num} hasn't been published yet. Latest comic is #{latest_num}.")
    
    comic = get_comic_by_number(comic_num)
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None,
                             error=f"Comic #{comic_num} could not be found. It may not exist.")


@app.route('/random')
def random_comic():
    # Redirect to a random comic
    latest_num = get_latest_comic_number()
    if not latest_num:
        return render_template('index.html', comic=None,
                             error="Couldn't fetch comic information. Please try again.")
    
    random_num = random.randint(1, latest_num)
    return show_comic(random_num)


@app.route('/next/<int:comic_num>')
def next_comic(comic_num):
    # Navigate to the next comic
    latest_num = get_latest_comic_number()
    if not latest_num:
        return render_template('index.html', comic=None,
                             error="Couldn't fetch comic information. Please try again.")
    
    next_num = comic_num + 1
    if next_num > latest_num:
        return render_template('index.html', comic=None,
                             error=f"This is the latest comic. No next comic available.")
    
    return show_comic(next_num)


@app.route('/prev/<int:comic_num>')
def prev_comic(comic_num):
    # Navigate to the previous comic
    prev_num = comic_num - 1
    if prev_num < 1:
        return render_template('index.html', comic=None,
                             error="This is the first comic. No previous comic available.")
    
    return show_comic(prev_num)


# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True, port=5001)
