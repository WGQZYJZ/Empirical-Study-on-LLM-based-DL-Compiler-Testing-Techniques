'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft2\ntorch.fft.rfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(5, 5)
print('input = ', input)
fft_input = torch.fft.rfft2(input)
print('fft_input = ', fft_input)