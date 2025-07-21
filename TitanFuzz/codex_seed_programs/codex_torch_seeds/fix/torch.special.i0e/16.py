'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0e\ntorch.special.i0e(input, *, out=None)\n'
import torch
import numpy as np
x = np.linspace((- 1), 1, num=100)
x = torch.from_numpy(x)
y = torch.special.i0e(x)
print(y)