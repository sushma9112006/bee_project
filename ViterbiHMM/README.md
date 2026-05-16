# ViterbiHMM

A computational biology project implementing the Viterbi algorithm using a Hidden Markov Model (HMM).

---

## Project Overview

This project predicts hidden biological states from observable events using probabilistic modeling and dynamic programming techniques.

The implementation demonstrates the working principle of Hidden Markov Models and sequence prediction algorithms frequently used in bioinformatics.

---

## Features

- Implements Hidden Markov Model
- Predicts hidden state sequences
- Calculates probability scores
- Uses dynamic programming approach
- Stores prediction results automatically

---

## Technologies Used

- Python 3
- NumPy

---

## Project Structure

```text
ViterbiHMM/
│
├── observations/
│   └── symptom_sequence.txt
│
├── predictions/
│   └── final_prediction.txt
│
├── state_prediction.py
├── README.md
└── .gitignore
```

---

## Run Project

```bash
python3 state_prediction.py
```

---

## Input

Observation sequence:

```text
warm tired shiver
```

---

## Output

Generated prediction file:

```text
predictions/final_prediction.txt
```

The output contains:

- observed events
- predicted hidden states
- probability of predicted hidden state sequence

---

## Computational Concept

Hidden Markov Models (HMMs) are probabilistic systems where:

- observable events are visible
- underlying states remain hidden

The Viterbi algorithm predicts the most likely hidden sequence responsible for generating observed data.

This approach is widely used in:

- gene prediction
- DNA annotation
- speech recognition
- sequence analysis
- computational biology