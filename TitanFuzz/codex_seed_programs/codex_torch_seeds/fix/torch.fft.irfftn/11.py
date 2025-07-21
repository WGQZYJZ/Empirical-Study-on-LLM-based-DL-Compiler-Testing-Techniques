'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfftn\ntorch.fft.irfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
x = np.random.rand(2, 3, 4, 5)
x = torch.tensor(x, dtype=torch.float32)
y = torch.fft.irfftn(x, s=None, dim=None, norm=None, out=None)
print(y)