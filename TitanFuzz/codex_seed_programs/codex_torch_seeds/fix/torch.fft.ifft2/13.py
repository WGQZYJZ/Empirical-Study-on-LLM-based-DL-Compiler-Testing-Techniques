'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft2\ntorch.fft.ifft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
from torch import fft
input = torch.randn(8, 8)
output = fft.ifft2(input)
print(output)