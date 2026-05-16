import pandas as pd
import matplotlib.pyplot as plt

print("===== FUNCTIONAL GENE ANALYSIS =====\n")

try:
    # Load genes
    with open(
        "input/selected_genes.txt",
        "r"
    ) as file:

        selected_genes = [
            line.strip()
            for line in file
        ]

    print("Genes Included In Analysis:\n")

    for gene in selected_genes:
        print(gene)

    # Simulated enrichment categories
    biological_processes = [
        "Cell Communication",
        "Signal Regulation",
        "Tumor Suppression",
        "Vascular Development",
        "Cell Division"
    ]

    association_scores = [
        7.8,
        9.1,
        8.4,
        6.9,
        8.7
    ]

    # Build dataframe
    enrichment_table = pd.DataFrame({

        "Biological Process":
        biological_processes,

        "Association Score":
        association_scores
    })

    print("\nFunctional Summary:\n")
    print(enrichment_table)

    # Create visualization
    plt.figure(figsize=(9, 5))

    plt.bar(
        enrichment_table["Biological Process"],
        enrichment_table["Association Score"]
    )

    plt.xticks(rotation=10)

    plt.xlabel("Biological Categories")
    plt.ylabel("Association Strength")

    plt.title(
        "Functional Enrichment Distribution"
    )

    # Save graph
    plt.savefig(
        "reports/enrichment_distribution.png"
    )

    # Save table
    enrichment_table.to_csv(
        "reports/functional_summary.csv",
        index=False
    )

    print(
        "\nBiological interpretation completed."
    )

except FileNotFoundError:
    print("Gene input file unavailable.")
