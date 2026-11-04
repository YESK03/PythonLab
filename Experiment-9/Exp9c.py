"""Experiment 9(c): K-Nearest Neighbors (KNN) classification.

A small, dependency-free machine-learning example using a flower dataset.
Each sample has two numeric features: petal length and petal width.
"""

from math import sqrt


# [petal length (cm), petal width (cm)]
TRAINING_DATA = [
    ([1.4, 0.2], "Setosa"),
    ([1.3, 0.2], "Setosa"),
    ([1.5, 0.4], "Setosa"),
    ([1.4, 0.3], "Setosa"),
    ([4.7, 1.4], "Versicolor"),
    ([4.5, 1.5], "Versicolor"),
    ([4.9, 1.5], "Versicolor"),
    ([4.6, 1.3], "Versicolor"),
    ([5.9, 2.1], "Virginica"),
    ([6.1, 2.5], "Virginica"),
    ([5.6, 2.2], "Virginica"),
    ([6.3, 1.8], "Virginica"),
]

TEST_DATA = [
    ([1.5, 0.2], "Setosa"),
    ([4.8, 1.6], "Versicolor"),
    ([6.0, 2.0], "Virginica"),
]


def euclidean_distance(point_a, point_b):
    """Return the straight-line distance between two feature vectors."""
    return sqrt(sum((a - b) ** 2 for a, b in zip(point_a, point_b)))


def predict(sample, training_data, k=3):
    """Predict a sample's class by majority vote among its k nearest neighbors."""
    if not training_data:
        raise ValueError("Training data must not be empty.")
    if not 1 <= k <= len(training_data):
        raise ValueError("k must be between 1 and the number of training samples.")

    neighbors = sorted(
        training_data,
        key=lambda item: euclidean_distance(sample, item[0]),
    )[:k]

    # In a tie, choose the label whose nearest matching neighbor is closest.
    votes = {}
    for features, label in neighbors:
        votes[label] = votes.get(label, 0) + 1
    return max(
        votes,
        key=lambda label: (
            votes[label],
            -next(
                euclidean_distance(sample, features)
                for features, neighbor_label in neighbors
                if neighbor_label == label
            ),
        ),
    )


def main():
    k = 3
    correct = 0

    print("K-Nearest Neighbors (KNN) Flower Classification")
    print(f"Number of neighbors (k): {k}\n")
    print("Test results:")

    for features, actual_label in TEST_DATA:
        predicted_label = predict(features, TRAINING_DATA, k)
        is_correct = predicted_label == actual_label
        correct += is_correct
        print(
            f"Features {features} | Actual: {actual_label:<10} "
            f"| Predicted: {predicted_label:<10} | "
            f"{'Correct' if is_correct else 'Incorrect'}"
        )

    accuracy = correct / len(TEST_DATA) * 100
    print(f"\nAccuracy: {correct}/{len(TEST_DATA)} ({accuracy:.1f}%)")

    new_flower = [5.1, 1.8]
    print(
        f"Predicted class for new flower {new_flower}: "
        f"{predict(new_flower, TRAINING_DATA, k)}"
    )


if __name__ == "__main__":
    main()
