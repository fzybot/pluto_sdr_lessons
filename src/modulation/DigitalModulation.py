"""@package class for Modulation and Demodulation functions for Digital Modulation

According to 3GPP TS 38.211 V16.10.0 p. 5.1 Modulatin mapper
implements function for digital modulation due to modulation order: BPSK, QPSK, [X]QAM. 
"""

from math import sqrt
import numpy as np

class DigitalModulation:
    """Digital Modulation.
 
    More details.
    """
    
    def __init__(self) -> None:
        """The constructor."""
        complex_array = np.array([],  dtype=complex)
        modulation_order = 0
        pass
    
    def modulate(self, modulation_order, bit_array):
        if modulation_order == 1:
            self.modulate_bpsk(bit_array)
        elif modulation_order == 2:
            self.modulate_qpsk(bit_array)
        return self.complex_array
    
    def modulate_bpsk(self, bit_array):
        """5.1.2 BPSK modulation
        """
        
        self.complex_array.resize( int(len(bit_array)) )
        
        for i in range(len(bit_array)):
            real = 1 / sqrt(2) * (1 - 2 * bit_array[i])
            imag = 1 / sqrt(2) * (1 - 2 * bit_array[i])
            self.complex_array[i] = complex(real, imag)
        return 0

    def modulate_qpsk(self, bit_array):
        """5.1.3 QPSK modulation
        """
        
        # TODO: нужна проверка на четность последовательности len(bit_array) mod 2 = 0
        
        self.complex_array.resize( int(len(bit_array) / 2) )
        # Modulation
        for i in range(0, len(bit_array), 2):
            real = 1 / sqrt(2) * (1 - 2 * bit_array[i])
            imag = 1 / sqrt(2) * (1 - 2 * bit_array[i + 1])
            self.complex_array[i] = complex(real, imag)
        
        return 0