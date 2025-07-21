'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftn\ntorch.fft.ifftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
a = torch.randn(3, 3, 3)
b = torch.randn(3, 3, 3)
c = torch.fft.ifftn(a, s=None, dim=None, norm=None, out=None)
print(c)