'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
import numpy as np
from torch import exp2
x = np.array([1, 2, 3, 4, 5])
x = torch.from_numpy(x)
y = exp2(x)
print(y)