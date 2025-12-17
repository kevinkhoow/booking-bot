# Web Automation Script

## Overview
This script uses Selenium WebDriver to navigate the interface of an appointment booking website. It monitors the website for the availability of appointments at certain dates and/or times and proceeds to book them when available. This script is not intended for commercial purposes.

## Project Structure
```
booking-bot
├── README.md  
└── bcd.py
```

## Setup

#### Clone the Repository
```
git clone https://github.com/kevinkhoow/booking-bot.git
cd booking-bot
```

### Edit Program with your Login Details
Edit lines 20-21 in `bcd.py` accordingly.
```
kname = 'your_username'
kpass = 'your_password'
```

### Install Dependencies
```
pip install selenium
```

### Execute Program
```
python3 bcd.py
```
