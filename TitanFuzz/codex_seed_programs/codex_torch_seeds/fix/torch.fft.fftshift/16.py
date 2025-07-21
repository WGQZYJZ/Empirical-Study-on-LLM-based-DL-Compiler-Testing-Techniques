'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
import numpy as np
import torch
import numpy as np
input_data = torch.randn(1, 2, 4, 4)
output = torch.fft.fftshift(input_data, dim=2)
print(input_data)
print(output)
print('input_data.shape = ', input_data.shape)
print('output.shape = ', output.shape)