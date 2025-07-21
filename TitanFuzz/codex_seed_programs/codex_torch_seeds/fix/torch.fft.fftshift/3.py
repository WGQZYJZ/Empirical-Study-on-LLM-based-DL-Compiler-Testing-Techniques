'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
import numpy as np
input = torch.randn(16, 16)
output = torch.fft.fftshift(input, dim=None)
print('input: ', input)
print('output: ', output)