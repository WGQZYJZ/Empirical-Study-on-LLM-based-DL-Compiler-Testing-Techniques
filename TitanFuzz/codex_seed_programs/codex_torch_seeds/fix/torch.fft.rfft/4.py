'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
import torch
x = torch.randn(1, 4, 8)
y = torch.fft.rfft(x)
print(y)