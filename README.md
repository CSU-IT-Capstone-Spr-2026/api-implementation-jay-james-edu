# XKCD Comic Viewer

This is a simple web application that allows users to view comics from XKCD, a popular webcomic by Randall Munroe. And this uses the official XKCD API to fetch and display comics.

## Features Implemented

Check off the features you implemented:

- [X] Feature #1: Display the Latest Comic
- [X] Feature #2: Display a Specific Comic by Number
- [X] Feature #3: Random Comic Button
- [X] Feature #4: Navigation (Previous/Next)
- [ ] Feature #5: Search by Comic Number Form
- [ ] Feature #6: Display Multiple Recent Comics

## Technologies Used

- Python 3.8+
- Flask 3.0.0
- Requests 2.31.0
- XKCD API

## Installation and Setup

### Prerequisites
- Python 3.8 or higher installed
- pip (Python package manager)

### Steps to Run

1. Clone or download this repository

2. Navigate to the project directory in your terminal:
   ```
   cd projectName
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and go to:
   ```
   http://localhost:5001
   ```

## Usage

View the Latest Comic:
When you first open the application, it automatically displays the most recent XKCD comic.

Get a Random Comic:
Click the "Random Comic" button to instantly jump to a randomly selected comic from the entire XKCD archive.

## Screenshots
<img width="1346" height="1353" alt="API 1" src="https://github.com/user-attachments/assets/2afeb534-939d-4d6d-a180-1419cd0aa53d" />
<img width="1305" height="1644" alt="API 2" src="https://github.com/user-attachments/assets/2acdc6aa-a804-4ded-98f1-ede17172fe11" />


## API Endpoints Used

- `GET /info.0.json` - Fetches the latest comic
- `GET /{comic_number}/info.0.json` - Fetches a specific comic by number

## Challenges and Solutions

 I learned that APIs have specific endpoints (like /info.0.json) that return structured JSON data, and understanding this structure is crucial for properly displaying the information. The XKCD API taught me about API rate limiting considerations even though it's a free API, making too many requests could potentially overload the server, which is why I implemented caching for the latest comic number. Also in this case, I did have to change the port number as I had an service that I forgot about running on 5000. But as soon I change the number, the website immediately popped up.

## Author

James Jay
