# 👾 Alien Invasion 🚀

**A space-themed arcade shooter built with Python and Pygame!**

Welcome to **Alien Invasion**, a classic arcade-style game where you control a spaceship, defend Earth, and battle waves of invading aliens! 🌌

This project is part of my journey learning Python, object-oriented programming, and game development.

---

## 🎮 About the Game

In Alien Invasion, you control a spaceship at the bottom of the screen while a fleet of aliens moves across the sky.

Your mission is simple: **destroy the aliens before they reach your ship or the bottom of the screen!**

### ✨ Features

- 🚀 **Spaceship movement** — Move left and right to dodge aliens.
- 🔫 **Laser shooting** — Fire bullets to destroy incoming enemies.
- 👾 **Alien fleets** — Battle rows of invading aliens.
- 💥 **Collision detection** — Destroy aliens by hitting them with bullets.
- ❤️ **Limited lives** — Survive with three ships.
- 🎵 **Background music** — Enjoy a space-themed soundtrack.
- 🔊 **Laser sound effects** — Hear your spaceship fire.
- 🐍 **Object-oriented design** — Built using organized Python classes.

---

## 🕹️ Controls

| Key | Action |
|---|---|
| ⬅️ Left Arrow | Move spaceship left |
| ➡️ Right Arrow | Move spaceship right |
| ␣ Spacebar | Fire laser |
| Q | Quit the game |

---

## 🛠️ Built With

- 🐍 **Python** — Core programming language
- 🎮 **Pygame** — Graphics, gameplay, input handling, and audio
- 🧠 **Object-Oriented Programming (OOP)** — Classes, methods, objects, and inheritance
- 📦 **Git & GitHub** — Version control and project management

---

## 🚀 Getting Started

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/cyberadryn/alien_invasion.git
```

Then navigate into the project:

```bash
cd alien_invasion
```

### 2. Install Python and Pygame

Make sure you have Python 3 installed.

Check your Python version:

```bash
python --version
```

Install Dependenices:

```bash
python -m pip install -r requirements.txt
```

### 3. Launch the Game

Run:

```bash
python3 alien_invasion.py
```

🎉 You're ready to defend Earth!

---

## 📁 Project Structure

```text
alien_invasion/
│
├── alien_invasion.py       # 🎮 Main game controller
├── settings.py             # ⚙️ Game configuration
├── game_stats.py           # ❤️ Player lives and statistics
├── ship.py                 # 🚀 Spaceship behavior
├── bullet.py               # 🔫 Bullet behavior
├── alien.py                # 👾 Alien behavior
├── sounds.py               # 🎵 Music and sound effects
│
├── images/                 # 🖼️ Game sprites
│
├── sounds/                 # 🔊 Audio files
│   ├── alien_invader_music.mp3
│   └── laser.wav
│
└── README.md               # 📖 Project documentation
```

---

## 🗺️ Future Improvements

Here are some features I'd like to explore as I continue developing the game:

- [ ] 🏆 Add a scoring system
- [ ] 🎚️ Add difficulty levels
- [ ] 👾 Introduce different alien types
- [ ] 💥 Add explosion animations and sounds
- [ ] ⏸️ Add pause and resume functionality
- [ ] 🏠 Create a main menu
- [ ] 🎮 Add a game-over screen
- [ ] 🔇 Add music and sound controls
- [ ] 🌟 Add visual effects and improved graphics

---

## 📝 Development Notes

This is a learning project, so I'll continue improving the code as I learn more about Python and game development.

Some features may change as I experiment with new ideas and techniques.

**Audio note:** If your system doesn't have an available audio device, the game is designed to continue running without sound when the mixer doesn't initialize.

---

## 💙 Thanks for Checking Out My Game!

Thanks for taking a look at Alien Invasion!

This project represents my progress learning to code, one feature and one bug fix at a time.

**Happy coding, and good luck defending Earth!** 🌎🚀👾
