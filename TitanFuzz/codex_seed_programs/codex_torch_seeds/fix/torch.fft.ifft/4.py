'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft\ntorch.fft.ifft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(1, 2, 4, dtype=torch.float32)
output = torch.fft.ifft(input)
print('input: \n', input)
print('output: \n', output)