'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft2\ntorch.fft.irfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import numpy as np
import torch
input = torch.randn(1, 2, 4, 4)
output = torch.fft.irfft2(input)
print(output)