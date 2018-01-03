import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


def main():
    logreg = LogisticRegression(random_state=42)
    X = np.load('./data/X.npy')
    Y = np.load('./data/Y.npy')
    scores = cross_val_score(logreg, X, Y, cv=5, verbose=1)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


if __name__ == '__main__':
    main()
