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

pluto_sdr_default_settings = {
    'ip_address': 'ip:192.168.2.1',
    'sample_rate': int(2.5e6),
}

def initialize_pluto_sdr(config_dict):
    ip = config_dict['ip_address']
    sample_rate = config_dict['sample_rate']
    
    sdr = adi.Pluto(ip)
    sdr.sample_rate = sample_rate
    print(sdr.sample_rate)
    return sdr

if __name__ == '__main__':
    pluto_ip = 'ip:192.168.2.1'
    sdr = initialize_pluto_sdr(pluto_sdr_default_settings)
    rx_data = sdr.rx()
    print("rx data length: ",len(rx_data))