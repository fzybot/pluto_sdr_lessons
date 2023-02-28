import adi
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

rx_default_settings = {
    'ip_address': 'ip:192.168.2.1',
    'sample_rate': int(1e6),
    'center_freq': 2412e6, # центральная частота: 2412 [MHz] или 2.412 [GHz]
    'num_samp': 100000,
    'gain_control_mode_chan0': 'manual',
    'rx_hardwaregain_chan0':  0.0,
}

tx_default_settings = {
    'ip_address': 'ip:192.168.2.1',
    'sample_rate': int(1e6),
    'center_freq': 915e6,
    'gain_control_mode_chan0': 'manual',
    'tx_hardwaregain_chan0':  -20.0,
}

def initialize_rx(config_dict):
    
    sdr = adi.Pluto(config_dict['ip_address'])
    sdr.sample_rate = config_dict['sample_rate']
    sdr.rx_lo = int(config_dict['center_freq'])
    sdr.rx_rf_bandwidth = int(config_dict['sample_rate'])
    sdr.rx_buffer_size = config_dict['num_samp']
    sdr.gain_control_mode_chan0 = config_dict['gain_control_mode_chan0']
    sdr.rx_hardwaregain_chan0 = config_dict['rx_hardwaregain_chan0']
    return sdr

def initialize_tx(config_dict):
    
    sdr = adi.Pluto(config_dict['ip_address'])
    sdr.sample_rate = config_dict['sample_rate']
    sdr.tx_lo = int(config_dict['center_freq'])
    sdr.gain_control_mode_chan0 = config_dict['gain_control_mode_chan0']
    sdr.tx_hardwaregain_chan0 = config_dict['tx_hardwaregain_chan0']
    return sdr
        
if __name__ == '__main__':
    sdr = initialize_rx(rx_default_settings)
    sample_rate = rx_default_settings['sample_rate']

    x_0 = []
    y_0 = []
    x_1 = []
    y_1 = []
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(9, 9))
    x_limit = 100
    y_limit = 10
    
    def animate(i):
        # Для очищения буфера rx() от мусора
        # TODO: проверить, мусор ли это или могут быть полезные данные.
        for i in range (0, 10):
            raw_data = sdr.rx()
        rx_data = sdr.rx()
        psd = np.abs(np.fft.fftshift(np.fft.fft(rx_data)))**2
        psd_dB = 10*np.log10(psd)
        f = np.linspace(sample_rate/-2, sample_rate/2, len(psd))
        ifft = np.abs(np.fft.ifft(rx_data))
            
        axs[0, 0].clear()
        axs[0, 0].plot(np.real(rx_data))
        axs[0, 0].plot(np.imag(rx_data))
        axs[0, 0].set_xlim([0,x_limit])
        axs[0, 0].set_ylim([-y_limit,y_limit])
        x_0.clear()
        y_0.clear()
        
        axs[1, 0].clear()
        axs[1, 0].plot(psd_dB)
        
        axs[1, 1].clear()
        axs[1, 1].plot(ifft)

    
    # run the animation
    ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=True)

    plt.show()
    