import random
from math import sin, cos, pi
import matplotlib.pyplot as plot
import timeit

N = 64
n = 12
freq = 1100


class WpkN:
    def __init__(self, w_real, w_image):
        self.w_real = w_real
        self.w_image = w_image

    def __str__(self):
        return str(self.w_real) + " - i*" + str(self.w_image)


def generate_signal():
    xS_arr = [0] * N
    for i in range(1, n + 1):
        A = random.random()
        phase = random.random()
        for j in range(N):
            xS_arr[j] += A * sin(freq/i * (j + 1) + phase)
    return xS_arr


def get_discrete_fourier_transform(signal: list):
    length = len(signal)
    return [sum((signal_X[j] * complex(cos(-2*pi*i*j/length), sin(-2*pi*i*j/length)) for j in range(length))) for i in range(N)]


#additional task
def gen_table_WpkN():
    table_WpkN = [[0 for col in range(N)] for row in range(N)]
    for i in range(N):
        for j in range(N):
            table_WpkN[i][j] = WpkN(cos(2 * pi * i * j / N), sin(2 * pi * i * j / N))


if __name__ == "__main__":
    signal_X = generate_signal()
    time_start = timeit.default_timer()
    gen_table_WpkN()
    print("Calculating table coefficients writing time: {}".format(timeit.default_timer() - time_start))
    time_start = timeit.default_timer()
    dft = get_discrete_fourier_transform(signal_X)
    print("Calculating DFT time: {}".format(timeit.default_timer() - time_start))
    figure, (xy1, xy2) = plot.subplots(2, figsize=(6, 12))
    xy1.plot(range(N), signal_X, "b")
    xy1.title.set_text("Signal")
    xy2.plot(range(N), dft, "r")
    xy2.title.set_text("DFT")
    plot.show()