import numpy as np
from math import sqrt


def euclidean_distance(x, y):
    """Calculate the Euclidean distance between two points or between two vectors"""
    a, b = np.array(x), np.array(y)
    edist = sqrt(np.sum((a-b)**2))

    return edist


def cosine_distance(x, y):
    """Calculate the cosine distance between two points or between two vectors"""
    a, b = np.array(x), np.array(y)
    cdist = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    return cdist