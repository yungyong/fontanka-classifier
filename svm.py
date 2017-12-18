import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score


def main():
    svm = SVC(kernel='linear')
    X = np.load('./data/X.npy')
    Y = np.load('./data/Y.npy')
    scores = cross_val_score(svm, X, Y, cv=5)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



if __name__ == '__main__':
    main()