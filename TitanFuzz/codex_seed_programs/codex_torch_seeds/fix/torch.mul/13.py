'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
c = torch.mul(torch.from_numpy(a), torch.from_numpy(b))
print(c)