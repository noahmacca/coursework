import numpy as np
import matplotlib.pyplot as plt

from util import getData

label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def main():
    print("entered main()")
    X, Y = getData(balance_ones=False)
    print("done loading data")

    while True:
        for i in range(7):
            x, y = X[Y==i], Y[Y==i]
            N = len(y)
            j = np.random.choice(N)
            plt.imshow(x[j].reshape(48, 48), cmap='gray')
            plt.title(label_map[y[j]])
            plt.show()
        prompt = raw_input('Quit? Enter Y:\n')
        if prompt == 'Y':
            break


if __name__ == '__main__':
    print("hello")
    main()
