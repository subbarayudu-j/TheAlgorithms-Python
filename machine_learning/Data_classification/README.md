# Simple KNN & Decision Tree Classifiers

This project demonstrates the implementation of the k-Nearest Neighbors (KNN) and Decision Tree algorithms from scratch in Python using a sample dataset of 2D points with binary class labels.

## Features

- **KNN Classifier:** Find the class of a test point using the majority class of the k nearest neighbors.
- **Decision Tree Classifier:** Build a decision tree classifier based on information gain and classify new data points.
- **Sample Dataset:** 50 manually defined (x, y, label) tuples.
- **Multiple Test Points:** Easily classify a list of new data points.

## Requirements

- Python 3.x
- (Optional) Libraries like numpy, pandas, scikit-learn, matplotlib for future enhancements.

See [`requirements.txt`](requirements.txt) for details.

## Usage

1. Clone this repository:

    ```
    git clone https://github.com/yourusername/simple-knn-decisiontree.git
    cd simple-knn-decisiontree
    ```

2. Run the classifiers:

    ```
    python knn_decision_tree.py
    ```

    You can modify the `test_points` list to classify different points.

## Files

- `knn_decision_tree.py`: Contains the implementations for KNN and Decision Tree, plus the sample dataset.
- `requirements.txt`: (Optional) Lists external libraries for extended functionality.
- `README.md`: Project introduction and usage.

## Extending the Project

- Integrate sklearn for quick benchmarking.
- Add plotting with matplotlib to visualize the dataset and decision boundaries.
- Use pandas for reading larger datasets from CSV files.

## License

MIT License

---

**Enjoy experimenting with classic machine learning algorithms!**
