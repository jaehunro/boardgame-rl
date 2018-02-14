# boardgame-rl
Various board games and reinforcement learning agent trained via Q-learning. The agent can be trained for various episodes and played against.

### Motivation
This project was completed in order to learn the basics of implementing Q-learning with a simple look up table for Q-values. Inspiration was taken from [Reinforcement Learning: An Introduction](https://mitpress.mit.edu/books/reinforcement-learning)

### Built with
- numpy

### Run instructions
```
python main.py -game tictactoe
```

### Test instructions
```
python -m unittest discover -v
```

![alt text](img/tictactoe_100.png "Tic Tac Toe RL Agent 100 Episodes")
![alt text](img/tictactoe_1000.png "Tic Tac Toe RL Agent 1000 Episodes")
![alt text](img/tictactoe_10000.png "Tic Tac Toe RL Agent 10000 Episodes")
![alt text](img/connectfour_100.png "Connect Four RL Agent 100 Episodes")
![alt text](img/connectfour_1000.png "Connect Four RL Agent 1000 Episodes")
![alt text](img/connectfour_10000.png "Connect Four RL Agent 10000 Episodes")

### Supported Board Games
- Tic Tac Toe
- Connect Four

### Implement Your Own Custom Game
Just add your game class to the game module and make sure it is a subclass of the Game abstract base class. Then just pass in your game to the rl agent.

### License
MIT  © [Jae Hun Ro](http://jaehunro.com)