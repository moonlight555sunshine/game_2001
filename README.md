# 🎲 Dice Duel

A fun terminal-based dice game where you play against the computer. First to reach 2001 points wins — but beware of the tricky effects of rolling 7 or 11!

## 🧩 Game Rules

- Both you and the computer roll two n-sided dice each round.
- The sum of your dice is added to your score.
- From the second round onward, special rules apply:
  - If you roll a 7, your score is divided by 7. 
  - If you roll an 11, your score is multiplied by 11. 
  - Any other result simply gets added to your score. 
- The first to reach 2001 or more points wins the game.

## 🔧 How It Works

- You enter your first dice and second dice.
- Supports rolling dice with common sizes: `D3`, `D4`, `D6`, `D8`, `D10`, `D12`, `D20`, `D100`
- If you enter an invalid input (e.g. `d3`, `D7`, etc.), the game will ask you to enter a valid input.
- Computer choises two a random size dice.

## ▶️ How to Run
1. Make sure Python 3 is installed on your system.
2. Save the script as `main.py`.
3. Run it using your terminal or command prompt:

   ```bash
   python main.py

## 💡 Example Round
```
Press ENTER to start
Enter your first dice code: D10
Enter your second dice code: D3
You rolled 7
Computer rolled 5
----------------------------------
Your points: 7
Computer points: 5
----------------------------------

Do you want continue? (Y/N) y
...
You win!

```
## 📥 Requirements

- Python 3.x
- No external libraries needed




