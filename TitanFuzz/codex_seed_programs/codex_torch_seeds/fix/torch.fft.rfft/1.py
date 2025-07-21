'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])
output = torch.fft.rfft(input_data)
print('Input data: ', input_data)
print('Output data: ', output)
'\nTask 4: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
output = torch.fft.irfft(input_data)
print('Input data: ', input_data)
print('Output data: ', output)