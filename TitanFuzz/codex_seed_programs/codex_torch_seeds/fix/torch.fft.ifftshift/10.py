'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftshift\ntorch.fft.ifftshift(input, dim=None)\n'
import torch
input = torch.randn(1, 5)
print('Input:', input)
output = torch.fft.ifftshift(input, dim=None)
print('Output:', output)