# Weather App

Welcome to the Weather App repository! By joining this workshop, you are taking your first step towards mastering Python, building REST APIs, and creating production-ready Python packages.

---

## Table of Contents

- [What You'll Learn](#what-youll-learn)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)

---

## What You'll Learn

- Web servers & HTTP status codes
- Client-server communication
- Query string parameters
- Frameworks: Flask & route handling
- APIs, API keys & authentication
- Python packaging, `requests` library, and `requirements.txt`

---

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)
- Internet connection

---

## Getting Started

### 1. Set Up Your Workspace

#### Open Your Terminal

- **macOS:** Open Launchpad, search for Terminal, and open it.
- **Windows:** Press `Win + R`, type `cmd`, and press Enter.

#### Clone the Repository

```sh
git clone https://github.com/TechWomenTribe/my_weather_app.git
cd my_weather_app
```

#### Create a Virtual Environment

If you don't already have a `venv` directory:

```sh
python -m venv venv
```

#### Activate the Virtual Environment

macOS/Linux:
```sh
source venv/bin/activate
```

Windows:
```sh
venv\Scripts\activate
```
### Install Dependencies
```sh
pip install -r requirements.txt
```

### Get a Weather API Key
1. Sign up at weatherapi.com.
2. After logging in, go to "My Account" (top right).
3. Copy your API key and keep it safe. Do not share your API key.
4. Don't worry we will explain it during the workshop. Trial is free!

<hr></hr>

## Usage
### Set your API key as an environment variable:
```sh
export WEATHER_API_KEY=your_api_key_here
```
### Run the app:
```sh
python app.py
```

### Example request:
Open your browser or use curl:
```sh
curl "http://127.0.0.1:5000/weather?city=London"
```

<hr></hr>

## Troubleshooting
- Module not found: Make sure your virtual environment is activated and dependencies are installed.
- Invalid API key: Double-check your API key and ensure it is set as an environment variable.
- Port already in use: Stop other apps using port 5000 or change the port in app.py.
<hr></hr>

## Contact
For questions or help, open an issue or contact your mentor.
<hr></hr>

You're now ready to start building!
Happy coding! 
