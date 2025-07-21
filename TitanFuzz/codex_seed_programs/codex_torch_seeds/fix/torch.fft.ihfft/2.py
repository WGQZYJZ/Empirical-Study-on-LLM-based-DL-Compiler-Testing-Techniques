'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ihfft\ntorch.fft.ihfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(4, 1, 8)
output = torch.fft.ihfft(input, n=None, dim=(- 1), norm=None, out=None)
print('input: ', input)
print('output: ', output)