'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(1, 2, 2, 2, 2)
input = torch.tensor(input, dtype=torch.float32)
output = torch.fft.fftn(input)
print(output)