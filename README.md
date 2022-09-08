# Coach price tracker
Tracks the coach prices for the Bristol to London route on Megabus, National Express and Flixbus.

# Objectives
Plot prices advertised on thse 3 bus operators over the course of 3 weeks, right up to the departure date. Find out what sorts of trends we see in their dynamic pricing algorithms, and try to buy the tickets at the optimal time(i.e. lowest price).

# Method of operation
1. scrape sites for price
2. log price in a database
3. plot historic prices over 3 weeks
4. have option to look at price for every week's trip

# Running
Install python dependencies:
```bash
poetry install
```

Run program:
```bash
poetry run python price_tracker/get_mega_bus_prices.py
```

# Stats

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)