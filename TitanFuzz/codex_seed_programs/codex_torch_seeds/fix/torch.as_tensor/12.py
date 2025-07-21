'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
import numpy as np
a = np.array([1, 2, 3])
print(a)
b = torch.as_tensor(a)
print(b)
c = torch.from_numpy(a)
print(c)
d = torch.tensor(a)
print(d)