import adi
import numpy as np
import matplotlib.pyplot as plt

# sdr = adi.Pluto('ip:192.168.2.1') # адрес PlutoSDR
# sdr.sample_rate = int(2.5e6)
# rx_data = sdr.rx()
# ifft = np.fft.ifft(rx_data)
# x_real_data = []
# y_imag_data = []
# print("rx data length: ",len(rx_data))
# print(ifft)
# for i in rx_data:
#     x_real_data.append(i.real)
#     y_imag_data.append(i.imag)
    
# plt.scatter(x_real_data, y_imag_data )
# plt.show()

def initialize_pluto_sdr(ip_address):
    sdr = adi.Pluto('ip:192.168.2.1')
    sdr.sample_rate = int(2.5e6)
    print(sdr.sample_rate)
    return sdr

if __name__ == '__main__':
    pluto_ip = 'ip:192.168.2.1'
    sdr = initialize_pluto_sdr(pluto_ip)
    rx_data = sdr.rx()
    print("rx data length: ",len(rx_data))