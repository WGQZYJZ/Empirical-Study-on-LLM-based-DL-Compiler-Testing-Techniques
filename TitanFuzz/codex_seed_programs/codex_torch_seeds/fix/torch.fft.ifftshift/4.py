'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftshift\ntorch.fft.ifftshift(input, dim=None)\n'
import torch
input = torch.randn(1, 2, 4, 4)
print(input)
print(torch.fft.fftshift(input, dim=1))
print(torch.fft.ifftshift(input, dim=1))