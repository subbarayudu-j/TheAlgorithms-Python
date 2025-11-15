import math
from collections import Counter

def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

def best_split(data):
    best_gain = 0
    best_feature = None
    best_threshold = None
    base_entropy = entropy([point[-1] for point in data])
    n_features = len(data[0]) - 1

    for feature in range(n_features):
        thresholds = set([point[feature] for point in data])
        for threshold in thresholds:
            left = [point for point in data if point[feature] <= threshold]
            right = [point for point in data if point[feature] > threshold]
            if not left or not right:
                continue
            p_left = len(left) / len(data)
            p_right = len(right) / len(data)
            gain = base_entropy - (p_left * entropy([point[-1] for point in left]) +
                                   p_right * entropy([point[-1] for point in right]))
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold
    return best_feature, best_threshold

def build_tree(data, depth=0, max_depth=5):
    labels = [point[-1] for point in data]
    if len(set(labels)) == 1 or depth >= max_depth:
        return Counter(labels).most_common(1)[0][0]  # Leaf node
    feature, threshold = best_split(data)
    if feature is None:
        return Counter(labels).most_common(1)[0][0]
    left = [point for point in data if point[feature] <= threshold]
    right = [point for point in data if point[feature] > threshold]
    return {
        "feature": feature,
        "threshold": threshold,
        "left": build_tree(left, depth + 1, max_depth),
        "right": build_tree(right, depth + 1, max_depth)
    }

def predict(tree, point):
    while isinstance(tree, dict):
        if point[tree["feature"]] <= tree["threshold"]:
            tree = tree["left"]
        else:
            tree = tree["right"]
    return tree

if __name__ == "__main__":
    data_points = [
        (5, 3, 0), (10, 15, 1), (8, 6, 0), (3, 7, 0), (12, 8, 1),
        (7, 14, 1), (4, 5, 0), (6, 9, 0), (14, 12, 1), (9, 11, 1),
        (11, 5, 0), (13, 7, 1), (6, 10, 0), (8, 13, 1), (5, 14, 1),
        (7, 4, 0), (10, 6, 0), (12, 9, 1), (9, 15, 1), (11, 13, 1),
        (3, 5, 0), (4, 10, 0), (14, 14, 1), (13, 9, 1), (8, 8, 0),
        (7, 7, 0), (15, 11, 1), (12, 6, 0), (9, 10, 0), (5, 13, 1),
        (6, 12, 1), (10, 10, 0), (13, 11, 1), (4, 8, 0), (3, 9, 0),
        (15, 13, 1), (14, 9, 1), (11, 7, 0), (8, 12, 1), (7, 13, 1),
        (5, 10, 0), (6, 11, 0), (9, 7, 0), (10, 9, 0), (12, 15, 1),
        (14, 13, 1), (15, 10, 1), (11, 12, 1), (4, 6, 0), (3, 8, 0)
    ]
    tree = build_tree(data_points, max_depth=5)
    test_points = [
        (2, 1), (5, 5), (11, 8), (7, 12), (14, 13), 
        (10, 9), (6, 10), (12, 12), (4, 7), (13, 14)
    ]
    for test_point in test_points:
        result = predict(tree, test_point)
        print(f"Predicted class for {test_point}: {result}")
