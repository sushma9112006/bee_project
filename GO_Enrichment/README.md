# GO_Enrichment

A bioinformatics project that performs simulated Gene Ontology (GO) enrichment analysis on selected genes.

---

## Project Overview

This project demonstrates how biological interpretation can be performed on a group of genes by associating them with functional biological categories.

The implementation generates enrichment summaries and visualizes biological associations using graphical analysis.

---

## Features

- Reads biological gene list
- Simulates enrichment analysis
- Generates enrichment score table
- Creates graphical enrichment visualization
- Stores results as CSV and image files

---

## Technologies Used

- Python 3
- pandas
- matplotlib

---

## Project Structure

```text
GO_Enrichment/
│
├── input/
│   └── selected_genes.txt
│
├── reports/
│   ├── enrichment_distribution.png
│   └── functional_summary.csv
│
├── biological_interpretation.py
├── README.md
└── .gitignore
```

---

## Run Project

```bash
python3 biological_interpretation.py
```

---

## Input

Gene list file:

```text
input/selected_genes.txt
```

Example genes:

- KRAS
- AKT1
- CDK2
- RB1
- VEGFA

---

## Output

Generated files:

```text
reports/enrichment_distribution.png
reports/functional_summary.csv
```

---

## Biological Concept

Gene Ontology (GO) enrichment analysis helps identify biological processes that appear frequently within a selected group of genes.

This allows researchers to discover:

- functional pathways
- biological mechanisms
- cellular processes
- disease-related activities

The project simulates this analytical workflow computationally.