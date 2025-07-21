'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0e\ntorch.special.i0e(input, *, out=None)\n'
import torch
import numpy as np
x = torch.tensor([(- 2), (- 1), 0, 1, 2])
y = torch.special.i0e(x)
print(y)
y_np = y.numpy()
print(y_np)
y_torch = torch.from_numpy(y_np)
print(y_torch)