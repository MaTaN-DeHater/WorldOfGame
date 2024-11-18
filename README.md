# World of Game

![Python](https://img.shields.io/badge/python-3.9+-blue.svg) ![Flask](https://img.shields.io/badge/flask-2.0+-green.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

A collection of engaging mini-games built with Python, featuring score tracking, a web-based leaderboard interface, and a fully automated CI/CD pipeline using modern DevOps tools.

## Overview

The **World of Game** project is not just about creating a collection of fun Python mini-games; it is also a showcase of my proficiency in modern DevOps practices. I've implemented **continuous integration**, **containerized environments**, **automated testing**, and **orchestrated deployments** to demonstrate my practical skills in DevOps. By using tools like **Jenkins**, **Docker**, **Docker Compose**, and **Selenium**, I've ensured that this project is scalable, reliable, and maintainable, all while highlighting my expertise in DevOps automation.

## Key Features

- **Multiple Games**:
  - Memory Game: Test your memory skills.
  - Number Guessing: Try to guess the secret number.
  - Currency Roulette: Convert currency values correctly.

- **Score System**:
  - Persistent points tracking based on difficulty levels.
  - Web-based leaderboard for user scores.

- **User Experience**:
  - Simple command-line interface with multiple difficulty levels.
  - Cross-platform compatibility for Windows, macOS, and Linux.

## DevOps and Automation Tools

This project demonstrates a complete DevOps workflow, featuring **CI/CD**, **containerization**, **automated testing**, and **orchestrated deployments**:

- **Jenkins Pipeline**: Automates the build, test, and deployment phases of the CI/CD process. This showcases my practical skills in continuous integration and delivery.
- **Docker & Docker Compose**: Every component is containerized to ensure consistent deployment across different environments. Docker Compose manages multi-container deployments, making it seamless to run the game and the web leaderboard.
- **Selenium**: Automated end-to-end testing of the web interface, ensuring a high-quality and reliable user experience.

These tools work in synergy to streamline the development and deployment process, minimizing manual errors, accelerating delivery, and ensuring an efficient CI/CD pipeline.

## CI/CD Pipeline and Containerization

The Jenkins pipeline and Docker integration demonstrate real-world automation and deployment techniques:

- **Continuous Integration**: Jenkins automates the building and testing of the code for every push, ensuring code quality and fast feedback.
- **Containerized Deployment**: Using **Docker** and **Docker Compose** helps create isolated environments that replicate production. This guarantees consistency between development, testing, and production environments.
- **Automated Testing**: **Selenium** is used to verify the functionality of the web-based leaderboard, providing confidence in the application through automated testing.

## Installation

To get started, clone the repository and install the dependencies.

1. Clone the repository:

   ```bash
   git clone https://github.com/Matan-Shabi/WorldOfGame.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Run the main game:
  
  ```bash
  python app.py
  ```

- View scores in the web browser:
  
  ```bash
  python main_score.py
  ```

## Running with Docker Compose

To run the project using Docker Compose, ensuring all components (game backend, web leaderboard interface) are orchestrated correctly:

```bash
docker-compose up --build
```

## Docker Image on Docker Hub

The Docker image for this project is available on Docker Hub:

[Docker Hub - World of Game](https://hub.docker.com/r/matanx/wog)

You can pull the image directly using:

```bash
docker pull matanx/wog
```

This command will build the Docker images and start the containers for the game service and web interface, ensuring seamless deployment.

## Project Structure

```
world-of-game/
├── games/
│   ├── memory_game.py
│   ├── guess_game.py
│   └── currency_game.py
├── tests/
│   ├── e2e.py
├── app.py
├── main_score.py
├── score.py
├── score.json
├── utils.py
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
└── README.md
```

## Technologies Used

- **Python 3.12**: Core language for the game logic.
- **Flask**: Lightweight web framework for the leaderboard interface.
- **JSON**: Simple score storage format.
- **Docker & Docker Compose**: Used for containerization, enabling consistent deployment and environment replication.
- **Jenkins**: Automates CI/CD pipelines, building, and testing processes.
- **Selenium**: Enables automated testing to verify game behavior and UI functionality.

## Contributing

Contributions are always welcome! To get started:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For more information or collaboration inquiries, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/matan-shabi/).

---



