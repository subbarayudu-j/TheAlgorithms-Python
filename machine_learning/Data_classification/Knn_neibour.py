
# Separate features and labels
def separate_features_labels(data):
    features = [point[:-1] for point in data]
    labels = [point[-1] for point in data]
    return features, labels

def euclidean_distance(point1, point2):
    return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5

def knn_classify(test_point, data_points, k):
    features, labels = separate_features_labels(data_points)
    distances = []
    
    for index, data_point in enumerate(features):
        distance = euclidean_distance(test_point, data_point)
        distances.append((distance, labels[index]))
    
    distances.sort(key=lambda x: x[0])
    k_nearest_labels = [label for _, label in distances[:k]]
    
    prediction = max(set(k_nearest_labels), key=k_nearest_labels.count)
    return prediction

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

    test_points = [
        (2, 1), (5, 5), (11, 8), (7, 12), (14, 13), 
        (10, 9), (6, 10), (12, 12), (4, 7), (13, 14)
    ]

    k = 5
    for test_point in test_points:
        prediction = knn_classify(test_point, data_points, k)
        print(f"The predicted class for the test point {test_point} is: {prediction}")
