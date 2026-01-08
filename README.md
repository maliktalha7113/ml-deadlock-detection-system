# ML-Based Deadlock Detection and Recovery System

This project simulates an intelligent operating system component that detects, predicts,
and recovers from deadlocks using classical OS algorithms and machine learning.

## Features
- Process and resource simulation
- Wait-For Graph deadlock detection
- Machine Learning-based deadlock prediction
- Automatic process recovery
- Professional Tkinter GUI
- Wait-For Graph visualization

## Technologies Used
- Python
- Scikit-learn
- Tkinter
- NetworkX
- Matplotlib

## How It Works
1. Processes request shared resources
2. Deadlocks are detected using Wait-For Graph cycles
3. Machine learning predicts deadlock risk in advance
4. Recovery manager terminates and restarts processes
5. GUI visualizes system behavior

## How to Run
```bash
python gui/app.py
