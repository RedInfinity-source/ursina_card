# CardConquest

Ursina Card Game is a multiplayer card game where players aim to lower the health of their opponents before they do the same. Players must manage their deck of cards wisely, monitor their health points, engage in turn-based combat, and race against the clock. The game features dynamic animation, randomized decks, multiplayer support, and an immersive UI. Players must adapt their strategies on the fly, draw new cards, and face unexpected challenges in head-to-head battles. The game's immersive UI adds an extra layer of urgency to the gameplay.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)
- [Rating: 8/10](#Rating)

# About

Ursina Card Game is a multiplayer card game where players aim to lower the health of their opponents before they do the same. Players must manage their deck of cards wisely, as each card represents a unique attack value. Player health is crucial, as it indicates their remaining vitality in the game. Turn-based combat is a key feature, where players strategically select cards from their hand to unleash devastating attacks and defend against enemy assaults. A timer adds urgency to decisions.
Features include dynamic animation, randomized decks, multiplayer support, and an immersive UI. Players can adapt their strategy on the fly as they draw new cards and face unexpected challenges. Multiplayer support allows players to challenge friends or AI opponents in head-to-head battles, showcasing their tactical prowess and card-playing skills. The game's rich visual environment features sleek UI elements and captivating card designs, bringing the game to life.

# Features

The Ursina Card Game is a multiplayer card game designed for competitive gameplay. Players compete against each other to lower their opponents' health before their own health depletes. They must strategically manage their deck of cards, each representing a unique attack value. Player health is a vital resource, requiring balance between offense and defense. The game operates on a turn-based system, with players strategically choosing cards during their turn. A timer adds urgency to decision-making, forcing players to think quickly and adapt their strategy within the time limit. The game features dynamic animations, allowing players to visually represent actions such as card plays, attacks, and health changes. Randomized decks ensure variety in gameplay, and players can challenge friends or AI opponents in head-to-head battles. The game environment is immersive, with sleek UI elements and captivating card designs. Overall, the Ursina Card Game combines strategy, competition, and visual appeal, making it an engaging experience for players.

# Imports

random, ursina

# Rating

It is divided into logical sections using functions and classes, enhancing readability and maintainability. Variable names are descriptive and follow a consistent naming convention, making it easier to understand the purpose of each variable. Additional comments could be beneficial in complex or critical sections.
The game logic handles player turns, health management, card effects, and the overall game flow effectively. Animations for card movements and hit effects add visual appeal and interactivity. However, the `exit()` function has a recursive call without a base case, which might lead to a stack overflow error.
The user interface (UI) is well-implemented with health bars, deck sizes, and the timer providing essential information to players. Hit animations and fading out of cards provide visual feedback, enhancing the gaming experience.
Suggestions for improvement include error handling mechanisms, code optimization, UI enhancements, documentation, and testing. Error handling mechanisms should be implemented to handle potential runtime errors gracefully, while code optimization should be considered for performance during animations or updates. UI enhancements should be improved to enhance the user experience, and documentation should be provided to explain complex logic and game rules.
