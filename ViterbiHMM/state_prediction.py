print("===== HIDDEN STATE ANALYZER =====\n")

# Hidden conditions
health_states = (
    "Stable",
    "Infected"
)

# Observable events
visible_events = (
    "warm",
    "tired",
    "shiver"
)

# Initial probabilities
initial_state_probability = {

    "Stable": 0.75,
    "Infected": 0.25
}

# Transition probabilities
state_change_probability = {

    "Stable": {
        "Stable": 0.65,
        "Infected": 0.35
    },

    "Infected": {
        "Stable": 0.30,
        "Infected": 0.70
    }
}

# Emission probabilities
event_probability = {

    "Stable": {
        "warm": 0.6,
        "tired": 0.3,
        "shiver": 0.1
    },

    "Infected": {
        "warm": 0.1,
        "tired": 0.4,
        "shiver": 0.5
    }
}


def calculate_hidden_path(

    observations,
    states,
    start_probability,
    transition_probability,
    emission_probability
):

    probability_matrix = [{}]

    path_tracker = {}

    # Initialize probabilities
    for current_state in states:

        probability_matrix[0][current_state] = (

            start_probability[current_state]
            * emission_probability[
                current_state
            ][observations[0]]
        )

        path_tracker[current_state] = [
            current_state
        ]

    # Main Viterbi loop
    for step in range(
        1,
        len(observations)
    ):

        probability_matrix.append({})

        updated_paths = {}

        for current_state in states:

            highest_probability, previous_state = max(

                (
                    probability_matrix[
                        step - 1
                    ][old_state]

                    * transition_probability[
                        old_state
                    ][current_state]

                    * emission_probability[
                        current_state
                    ][observations[step]],

                    old_state
                )

                for old_state in states
            )

            probability_matrix[
                step
            ][current_state] = (
                highest_probability
            )

            updated_paths[
                current_state
            ] = (

                path_tracker[
                    previous_state
                ] + [current_state]
            )

        path_tracker = updated_paths

    # Final state selection
    final_probability, best_state = max(

        (
            probability_matrix[
                len(observations) - 1
            ][state],

            state
        )

        for state in states
    )

    return (
        final_probability,
        path_tracker[best_state]
    )


# Execute algorithm
probability_score, predicted_path = (

    calculate_hidden_path(

        visible_events,
        health_states,
        initial_state_probability,
        state_change_probability,
        event_probability
    )
)

print("Observed Events:\n")
print(visible_events)

print("\nPredicted Hidden States:\n")
print(predicted_path)

print("\nFinal Probability Score:\n")
print(probability_score)

# Save results
with open(
    "predictions/final_prediction.txt",
    "w"
) as prediction_file:

    prediction_file.write(
        "Observed Events:\n"
    )

    prediction_file.write(
        str(visible_events)
    )

    prediction_file.write(
        "\n\nPredicted States:\n"
    )

    prediction_file.write(
        str(predicted_path)
    )

    prediction_file.write(
        "\n\nProbability Score:\n"
    )

    prediction_file.write(
        str(probability_score)
    )

print("\nPrediction results stored successfully.")
