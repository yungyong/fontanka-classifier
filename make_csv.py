import os
import pandas as pd
import numpy as np

def main():
    files = os.listdir('./data/cleaned')
    data = []
    for file in files:
        with open('./data/cleaned/' + file, 'r') as f:
            category = f.readline().strip()
            content = f.read().strip()
            data.append((category, content))
    pd.DataFrame(
        data=data,
        columns=('Category', 'Content'),
        index=np.arange(len(data))
    ).to_csv('./data/cleaned.csv', index=None)


if __name__ == '__main__':
    main()