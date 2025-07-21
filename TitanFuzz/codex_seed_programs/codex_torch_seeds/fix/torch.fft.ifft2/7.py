'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft2\ntorch.fft.ifft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
input = torch.randn(2, 3, 4, 5, 2)
print('Input tensor: ', input)
print('Task 3: Call the API torch.fft.ifft2')
output = torch.fft.ifft2(input)
print('Output tensor: ', output)