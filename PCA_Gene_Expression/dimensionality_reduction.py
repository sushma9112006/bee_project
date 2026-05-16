import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

print("===== CELLULAR EXPRESSION REDUCTION =====\n")

try:
    # Load dataset
    biological_data = pd.read_csv(
        "datasets/cellular_expression.csv"
    )

    print("Loaded Dataset:\n")
    print(biological_data)

    # Store labels
    gene_labels = biological_data["Gene"]

    # Remove text column
    numerical_values = biological_data.drop(
        columns=["Gene"]
    )

    # PCA model
    reducer = PCA(n_components=2)

    compressed_output = reducer.fit_transform(
        numerical_values
    )

    # Convert to dataframe
    reduced_dataset = pd.DataFrame(
        compressed_output,
        columns=["Component_A", "Component_B"]
    )

    reduced_dataset["Gene"] = gene_labels

    print("\nReduced Dataset:\n")
    print(reduced_dataset)

    # Create plot
    plt.figure(figsize=(8, 6))

    plt.scatter(
        reduced_dataset["Component_A"],
        reduced_dataset["Component_B"]
    )

    # Add labels
    for idx, gene in enumerate(
        reduced_dataset["Gene"]
    ):

        plt.annotate(
            gene,
            (
                reduced_dataset["Component_A"][idx],
                reduced_dataset["Component_B"][idx]
            )
        )

    plt.title("Compressed Gene Expression Space")

    plt.xlabel("Component A")
    plt.ylabel("Component B")

    # Save figure
    plt.savefig(
        "visuals/expression_projection.png"
    )

    print(
        "\nProjection image generated successfully."
    )

except FileNotFoundError:
    print("Expression dataset could not be found.")
