# PCA_Gene_Expression

A bioinformatics project that performs Principal Component Analysis (PCA) on multidimensional gene expression datasets.

---

## Project Overview

This project analyzes biological expression data and reduces high-dimensional measurements into two principal components for visualization and interpretation.

The implementation demonstrates dimensionality reduction techniques commonly used in computational biology and machine learning.

---

## Features

- Reads gene expression dataset from CSV file
- Performs PCA dimensionality reduction
- Visualizes compressed gene expression patterns
- Generates scatter projection graph
- Saves graphical output automatically

---

## Technologies Used

- Python 3
- pandas
- matplotlib
- scikit-learn

---

## Project Structure

```text
PCA_Gene_Expression/
│
├── datasets/
│   └── cellular_expression.csv
│
├── visuals/
│   └── expression_projection.png
│
├── dimensionality_reduction.py
├── README.md
└── .gitignore
```

---

## Run Project

```bash
python3 dimensionality_reduction.py
```

---

## Dataset Description

The dataset contains simulated biological expression values measured across different tissues.

Example columns:

- Brain
- Heart
- Liver
- Kidney

Each row represents a gene and its expression profile.

---

## Output

The project generates:

- Reduced PCA coordinates
- Scatter visualization image

Output file:

```text
visuals/expression_projection.png
```

---

## Biological Concept

Gene expression datasets often contain many dimensions and variables.

Principal Component Analysis (PCA) reduces these dimensions while preserving most of the variation in the data.

This helps researchers:

- identify biological patterns
- visualize clustering
- simplify complex datasets