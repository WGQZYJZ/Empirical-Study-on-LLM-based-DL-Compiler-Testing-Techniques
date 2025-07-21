'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft2\ntorch.fft.rfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import torch.fft
input = torch.randn(16, 8)
output = torch.fft.rfft2(input)
print(output)