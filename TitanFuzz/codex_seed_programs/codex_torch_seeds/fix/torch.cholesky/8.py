'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky\ntorch.cholesky(input, upper=False, *, out=None)\n'
import torch
import numpy as np
a = torch.tensor([[4.0, 12.0, (- 16.0)], [12.0, 37.0, (- 43.0)], [(- 16.0), (- 43.0), 98.0]])
print(a)
b = torch.cholesky(a, upper=False)
print(b)
c = torch.mm(b, torch.t(b))
print(c)
print(a)