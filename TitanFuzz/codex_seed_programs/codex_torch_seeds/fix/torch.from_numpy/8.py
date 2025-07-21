'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
a = np.array([1, 2, 3])
print(a)
b = torch.from_numpy(a)
print(b)
c = np.array([1, 2, 3])
d = torch.from_numpy(c)
print(d)
e = np.array([1, 2, 3])
f = torch.from_numpy(e)
print(f)
g = np.array([1, 2, 3])
h = torch.from_numpy(g)
print(h)
i = np.array([1, 2, 3])
j = torch.from_numpy(i)
print(j)