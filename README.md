# Airline Points Price Scraper API

A simple API built with Flask that scrapes the current prices of points for various airline loyalty programs from [MaxMilhas](https://www.maxmilhas.com.br/vender-milhas) using Selenium and BeautifulSoup. The API returns the latest prices for each airline program in a JSON format.

## Features

- Scrapes the most recent point prices from MaxMilhas.
- Returns a JSON with airline loyalty program names and corresponding prices.
- Built using Flask, Selenium, and BeautifulSoup.
- Headless Chrome browser used for scraping.

## How it Works

1. The API sends a request to the MaxMilhas page.
2. It uses Selenium to load the page and BeautifulSoup to parse the HTML content.
3. Scrapes the airline program names and their point prices.
4. Returns a dictionary of the program names and prices.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/airline-points-scraper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd airline-points-scraper
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Make sure you have Chrome installed on your machine and set up the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Selenium.

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. The API will be available at `http://localhost:5000/`. You can make a GET request to this endpoint, and the current point prices will be returned in a JSON-like format.

## Example Output

```json
{
  "Program A": "R$ 22,00",
  "Program B": "R$ 18,50",
  "Program C": "R$ 25,00"
}
