'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
import numpy as np
x = torch.arange(0, 16).reshape(4, 4)
y = torch.fft.fftshift(x)
print(x)
print(y)
x_np = np.arange(0, 16).reshape(4, 4)
y_np = np.fft.fftshift(x_np)
print(y_np)