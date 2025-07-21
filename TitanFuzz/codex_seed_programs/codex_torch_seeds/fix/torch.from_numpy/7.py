'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
b = torch.from_numpy(a)
print(b)
c = b.numpy()
print(c)