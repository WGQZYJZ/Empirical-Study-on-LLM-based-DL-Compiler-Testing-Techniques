'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
x = np.random.randn(3, 4, 5)
x = torch.from_numpy(x)
y = torch.fft.rfftn(x, s=None, dim=None, norm=None, out=None)
print(y)