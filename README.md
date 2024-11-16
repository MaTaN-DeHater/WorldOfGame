# World of Game

![Python](https://img.shields.io/badge/python-3.9+-blue.svg) ![Flask](https://img.shields.io/badge/flask-2.0+-green.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

A collection of engaging mini-games built with Python, featuring score tracking, a web-based leaderboard interface, and a fully automated CI/CD pipeline using modern DevOps tools.

## Overview

The **World of Game** project is not just a collection of fun and engaging Python games, but also a showcase of modern software development practices. It features continuous integration, containerized environments, and automated testing to demonstrate practical DevOps skills. The project integrates tools like **Jenkins**, **Docker**, and **Selenium** to ensure scalability, reliability, and maintainability, making it an ideal demonstration of DevOps automation expertise.

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

- **DevOps Integration**:
  - Automated build and deployment using **Jenkins Pipeline**.
  - Containerized application with **Docker** and orchestrated with **Docker Compose**.
  - **Automated End-to-End Testing** with **Selenium**.

## DevOps and Automation Tools

This project leverages a variety of tools to demonstrate a complete DevOps workflow:

- **Jenkins Pipeline**: Automates the build and testing phases of the CI/CD process, showcasing skills in continuous integration and delivery.
- **Docker and Docker Compose**: Containerize each component for consistent deployment across environments, with Docker Compose managing multi-container deployments.
- **Selenium**: Automated testing of the web interface to ensure high-quality and reliable user experiences.

These tools are integrated to provide a streamlined, automated development process, ensuring faster releases, reduced manual errors, and an efficient deployment pipeline.

## Installation

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

- **Python 3.12**: Core language for the games.
- **Flask**: Lightweight web framework for the leaderboard interface.
- **JSON**: Simple score storage format.
- **Docker & Docker Compose**: Containerization for consistent deployment.
- **Jenkins**: CI/CD pipeline to automate builds and testing.
- **Selenium**: Automated testing to verify game behavior.

## CI/CD Pipeline and Containerization

The Jenkins pipeline and Docker integration demonstrate real-world automation and deployment techniques:

- **Build Automation**: Jenkins automates building and testing the code on each push, ensuring quality.
- **Containerization**: Docker is used to create isolated environments, ensuring consistency across development, testing, and production.
- **Deployment Orchestration**: Docker Compose brings all components together seamlessly, facilitating testing and scalability.

## Running with Docker Compose

To run the project using Docker Compose, ensuring all components (backend, web interface) are orchestrated correctly:

```bash
docker-compose up --build
```

This will build the Docker images and start the containers for the game service and web interface.

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For more information or collaboration inquiries, please feel free to reach out via [LinkedIn](https://www.linkedin.com/in/matan-shabi/).

---

