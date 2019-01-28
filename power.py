import numpy as np
import pandas as pd

def power(sample1, sample2, reps, size, alpha):
    count = 0
    for i in range(0, reps):
        random_sample1 = []
        random_sample2 = []
        for x in range(0, size):
            random_sample1.append(sample1[np.random.randint(0, len(sample1))])
            random_sample2.append(sample2[np.random.randint(0, len(sample2))])
        cat_arr = np.concatenate((random_sample1, random_sample2))
        np.random.shuffle(cat_arr)
        random_shuffle_sample1 = cat_arr[:size]
        random_shuffle_sample2 = cat_arr[size:]
        if abs(np.mean(random_shuffle_sample1) - np.mean(random_shuffle_sample2)) < 1-alpha:
            count += 1
    return count / reps

if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv').dropna()
    sample1 = df.values.T[0]
    sample2 = df.values.T[1]
    print(power(sample1, sample2, 1000, 10, 0.95))
