# Macgyver-maze

In this game, you'll help MacGyver to escape a maze by killing a guard with a crafted syringe

### Installation:

- To install and run this app, clone the repository by running:
```bash
git clone https://github.com/Manifest42/Macgyver-maze.git
```
    
- Install virtualenv if it's not already done:
```bash
pip3 install virtualenv
```
- Create a virtual environment by running:
```bash
virtualenv venv
```
- Activate the virtual environment by running:
```bash
source venv/bin/activate
```
- If you're not already there move to the root of the application:
```bash
cd Macgyver-maze-master
``` 
- Install the requirements by running:
```bash
pip3 install -r requirements.txt
```
- Run the program by running:
```bash
python3 main.py
```

### Map customization:

- You'll find it in a file named "sample_map.txt" in the directory "maps".

- The size has to remain the same: 15 lines and 15 colums.

        - x for a wall
        - blank space for a path
        - P for player's starting position
        - E for the enemy
        - G for the goal
   
### Controls:

- Use the arrow keys to move
- Walk on items to grab them
- Walk on the guard once you have the syringue to kill him

### Goal:

- Reach the maze's exit.
     
- To kill the guard, you'll need a weapon: a deadly syringue ! To do it in Macgyver's style, find three items scattered into the maze: a needle, a plactic tube and a bottle fill of ether.
