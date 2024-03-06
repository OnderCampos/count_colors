from PIL import Image
import io
import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.cluster import AffinityPropagation
from sklearn import metrics


"""
create a python program that do the follow:
1) Get the countorns of the image
2) For every countorn calculate the mean value, 
considering if a contorn is inside another do not consider the inner countorns in the mean 

"""

def affinityPropagation(image):
    print("hello", image)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)  # Convert to RGB format for compatibility
    print(image)
    pixels = image.reshape((-1, 3))

    pixels = np.float32(pixels)


    pixels /= 255.0

    similarity_matrix = -metrics.pairwise_distances(pixels, metric='euclidean')

    affinity_propagation = AffinityPropagation(damping=0.5)
    affinity_propagation.fit(similarity_matrix)

    cluster_labels = affinity_propagation.labels_
    exemplars = affinity_propagation.cluster_centers_indices_
    print(exemplars)
    return np.array([])


def meanShift(image):

    image_array = np.array(image)

    if len(image_array.shape) == 3 and image_array.shape[2] == 3:
        pixels = image_array.reshape((-1, 3))
    else:

        image = image.convert('RGB')
        image_array = np.array(image)
        pixels = image_array.reshape((-1, 3))

    bandwidth = estimate_bandwidth(pixels, quantile=0.2, n_samples=500)


    ms = MeanShift(bandwidth=bandwidth)
    ms.fit(pixels)

    cluster_centers = ms.cluster_centers_
    #labels = ms.labels_

    # Number of clusters found
    #n_clusters = len(np.unique(labels))
    print(cluster_centers)
    return cluster_centers

def extract_colors3(image, max_iterations=30, initial_clusters=5, max_clusters=20):
    best_score = float('inf')
    best_labels = None
    best_centroids = None
    best_k = 0
    image_array = np.array(image)

    if len(image_array.shape) == 3 and image_array.shape[2] == 3:
        pixels = image_array.reshape((-1, 3))
    else:
        image = image.convert('RGB')
        image_array = np.array(image)
        pixels = image_array.reshape((-1, 3))

    for k in range(initial_clusters, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, max_iter=max_iterations)
        kmeans.fit(pixels)

        labels = kmeans.labels_
        centroids = kmeans.cluster_centers_

        inertia = kmeans.inertia_

        print(inertia, best_score)
        if inertia < best_score:
            best_score = inertia
            best_labels = labels
            best_centroids = centroids
            best_k = k

    return  best_centroids.tolist()

def extract_colors2(image, max_clusters=20):
    # Supervised 
    thumbnail_size = (100, 100)
    thumbnail = image.copy().resize(thumbnail_size)

    image_array = np.array(thumbnail)

    if len(image_array.shape) == 3 and image_array.shape[2] == 3:
        pixels = image_array.reshape((-1, 3))
    else:
        image = image.convert('RGB')
        image_array = np.array(image)
        pixels = image_array.reshape((-1, 3))
    kmeans = KMeans(n_clusters=max_clusters, random_state=42)
    kmeans.fit(pixels)
    dominant_colors = kmeans.cluster_centers_.astype(int)

    return dominant_colors


def extract_colors(image):
    #All the colors
    thumbnail_size = (100, 100)
    thumbnail = image.copy().resize(thumbnail_size)

    if thumbnail.mode in ("P", "PA"):
        palette = thumbnail.getpalette()

        rgb_values = [palette[i:i + 3] for i in range(0, len(palette), 3)]

        return set(rgb_values)
    else:

        thumbnail = thumbnail.convert("RGB")

        rgb_values = list(thumbnail.getdata())

        return set(rgb_values)
