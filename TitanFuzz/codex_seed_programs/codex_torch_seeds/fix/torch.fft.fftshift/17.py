'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
import torch.nn.functional as F
x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
print('Input data: ', x)
y = torch.fft.fftshift(x, dim=0)
print('Output data: ', y)