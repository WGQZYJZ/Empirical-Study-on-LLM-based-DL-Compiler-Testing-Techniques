'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(3, 4, 5, 6)
y = torch.fft.fftn(x, norm=None)
print(y)