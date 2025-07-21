'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
a = np.random.randn(1, 4, 4)
a = torch.tensor(a, dtype=torch.float64)
print('Input data: ', a)
b = torch.fft.rfft(a, n=None, dim=(- 1), norm=None, out=None)
print('Output data: ', b)