'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
import numpy as np
input_data = torch.rand(2, 3, 4)
print('Input data: ', input_data)
output_data = torch.fft.fftshift(input_data, dim=None)
print('Output data: ', output_data)