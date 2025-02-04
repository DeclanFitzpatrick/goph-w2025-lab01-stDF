import numpy as np
import matplotlib.pyplot as plt

def main():
    #load seismic data
    data = np.loadtxt("C:/Users/Declan/repos/goph-w2025-lab01-stDF/data/s_wave_data.txt")
    t_data = data[:,0]
    v_data = data[:,1]
    v2_data = v_data**2

    plt.figure(figsize=(6,8))

    plt.subplot(2, 1, 1)
    plt.plot(t_data, v_data, "-b", label="s_wave_data")
    plt.xlabel("time, t [s]")
    plt.ylabel("velocity, v [mm/s]")
    plt.legend

    plt.subplot(2, 1, 2)
    plt.plot(t_data, v2_data, "-b", label="s_wave_data")
    plt.xlabel("time, t [s]")
    plt.ylabel("sq velocity, v**2 [mm/s]")
    plt.legend()

    plt.savefig("C:/Users/Declan/repos/goph-w2025-lab01-stDF/figures/s_wave_data.png")

if __name__ == "__main__":
    main()