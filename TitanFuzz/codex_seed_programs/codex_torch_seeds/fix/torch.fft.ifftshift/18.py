'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftshift\ntorch.fft.ifftshift(input, dim=None)\n'
import torch
x = torch.randn(3, 4, 5)
print('Input data: ', x)
y = torch.fft.ifftshift(x)
print('Output data: ', y)