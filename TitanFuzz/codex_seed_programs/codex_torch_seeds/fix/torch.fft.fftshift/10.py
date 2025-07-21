'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
input = torch.randn(3, 4, 5)
print(input)
output = torch.fft.fftshift(input)
print(output)
output = torch.fft.fftshift(input, 2)
print(output)