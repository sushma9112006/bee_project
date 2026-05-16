# Gene2protein

A bioinformatics project developed using Python and BioPython for translating DNA sequences into protein sequences.

---

## Project Overview

This project reads a nucleotide sequence from a text file, validates the DNA sequence, translates it into its corresponding amino acid chain, and stores the translated protein sequence in an output file.

The project demonstrates a simple implementation of biological sequence translation using computational methods.

---

## Features

- Reads DNA sequence from external file
- Validates nucleotide characters
- Converts DNA into amino acid sequence
- Saves translated protein output
- Handles invalid input gracefully

---

## Technologies Used

- Python 3
- BioPython

---

## Project Structure

```text
Gene2protein/
│
├── sequences/
│   └── sample_sequence.txt
│
├── results/
│   └── protein_result.txt
│
├── translator.py
├── README.md
└── .gitignore
```

---

## Input File

```text
sequences/sample_sequence.txt
```

Example input:

```text
ATGAAACGTTGGGCTTAA
```

---

## Output File

```text
results/protein_result.txt
```

Example output:

```text
MKRWAL
```

---

## Run Project

```bash
python3 translator.py
```

---

## Biological Concept

DNA sequences contain genetic information encoded using four nucleotide bases:

- A → Adenine
- T → Thymine
- G → Guanine
- C → Cytosine

During translation, groups of three nucleotides (codons) are converted into amino acids, forming a protein sequence.

This project simulates that biological process computationally.