import time

import adi
import matplotlib.pyplot as plt
import numpy as np


# Попробуем отправить просто 1 синусоиду и принять ее же
sample_rate = 1e6 # Hz ширина полосы
20 Mhz = 30.7 Msps
center_freq = 2500e6# Hz
num_samps = 10000 # number of samples per call to rx()

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)

# Config Rx
sdr.rx_lo = int(center_freq)
sdr.tx_lo = int(center_freq)
sdr.rx_buffer_size = num_samps

print(sdr.rx())

for r in range(10):
    rx = sdr.rx()
    plt.clf()
    plt.plot(rx.real)
    plt.plot(rx.imag)
    plt.draw()
    plt.pause(0.05)
    time.sleep(0.1)

plt.show()

# [-19.+23.j -18.+36.j -13.+25.j ...  10. -3.j  -2. -6.j   2.-16.j]

[-161.-429.j  226. +19.j -130.-376.j ...    3. -12.j   19.  -2.j
  -42. -50.j]