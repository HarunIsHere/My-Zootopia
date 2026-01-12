# My-Zootopia (API)

Generates a simple animals website (`animals.html`) based on animal data fetched from the API Ninjas Animals API.

## Requirements

- Python 3
- Dependencies listed in `requirements.txt`

## Setup

1. Install dependencies:

    pip install -r requirements.txt

2. Create a `.env` file in the project root with your API key:

    API_KEY='YOUR_API_KEY_HERE'

## Usage

Run the generator:

    python3 animals_web_generator.py

Enter an animal name (e.g., `Fox`). The program generates `animals.html` in the project folder.

## Project Structure

- `animals_web_generator.py` — website generator (templates + HTML output)
- `data_fetcher.py` — fetches animal data from the API
- `animals_template.html` — HTML template
- `requirements.txt` — dependencies
