import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import numpy as np


def main():
    news_files = os.listdir('./data/cleaned')
    categories = []
    contents = []
    for file in news_files:
        with open('./data/cleaned/' + file, 'r') as f:
            categories.append(f.readline().strip())
            contents.append(f.read().strip())

    tfidf = TfidfVectorizer(
        input='content',
        lowercase=False,
        min_df=0.1,
        use_idf=True,
        smooth_idf=True,
        sublinear_tf=True,
        max_features=10000
    )

    x = tfidf.fit_transform(contents)
    x = x.todense()

    le = LabelEncoder()
    y = le.fit_transform(categories)

    np.save('./data/X', x)
    np.save('./data/Y', y)
    np.save('./data/classes', le.classes_)

    print('Classes:')
    for cls in le.classes_:
        print(' - ' + cls)


if __name__ == '__main__':
    main()