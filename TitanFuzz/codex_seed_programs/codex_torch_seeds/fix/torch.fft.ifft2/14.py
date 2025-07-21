'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft2\ntorch.fft.ifft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import numpy as np
(N, C, H, W) = (2, 3, 4, 4)
input = torch.randn(N, C, H, W)
output = torch.fft.ifft2(input, s=None, dim=((- 2), (- 1)), norm=None, out=None)
print(output)