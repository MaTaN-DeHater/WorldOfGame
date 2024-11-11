# World of Game

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A collection of engaging mini-games built with Python, featuring score tracking and a web-based leaderboard interface.

## Features

- **Multiple Games**:
  - Memory Game - Test your memory skills
  - Number Guessing - Try to guess the secret number
  - Currency Roulette - Convert currency values
  
- **Score System**:
  - Points based on difficulty level
  - Persistent score tracking
  - Web-based leaderboard
  
- **User Experience**:
  - Simple command-line interface
  - Multiple difficulty levels
  - Cross-platform compatibility

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/world-of-game.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main game:
```bash
python app.py
```

View scores in web browser:
```bash
python main_score.py
```

## Project Structure

```
world-of-game/
├── games/
│   ├── memory_game.py
│   ├── guess_game.py
│   └── currency_game.py
├── utils/
│   ├── score.py
│   ├── score.json
│   └── utils.py
├── tests/
│   ├── e2e.py
├── app.py
├── main_score.py
├── Dockerfile
├── Docker-compose.yml
├── requirements.txt
└── README.md
```

## Technologies

- Python 3.12
- Flask (Web Framework)
- JSON (Score Storage)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```


