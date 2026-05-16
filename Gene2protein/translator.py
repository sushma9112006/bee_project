from Bio.Seq import Seq

print("===== SEQUENCE TRANSLATION SYSTEM =====\n")

try:
    # Read sequence file
    with open(
        "sequences/sample_sequence.txt",
        "r"
    ) as sequence_file:

        nucleotide_chain = (
            sequence_file.read()
            .strip()
            .upper()
        )

    # Allowed DNA letters
    valid_symbols = {"A", "T", "G", "C"}

    # Validation check
    if not set(nucleotide_chain).issubset(valid_symbols):
        raise ValueError(
            "Sequence contains unsupported symbols."
        )

    print("DNA Input:\n")
    print(nucleotide_chain)

    # Convert sequence
    dna_sequence = Seq(nucleotide_chain)

    protein_output = dna_sequence.translate()

    print("\nTranslated Protein:\n")
    print(protein_output)

    # Save result
    with open(
        "results/protein_result.txt",
        "w"
    ) as result_file:

        result_file.write(
            str(protein_output)
        )

    print("\nTranslation saved successfully.")

except FileNotFoundError:
    print("Sequence input file not located.")

except ValueError as issue:
    print("Validation Error:", issue)
