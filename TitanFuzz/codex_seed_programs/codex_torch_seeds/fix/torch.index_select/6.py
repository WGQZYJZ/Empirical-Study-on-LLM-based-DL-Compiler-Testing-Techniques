'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(3, 4)
print(x)
indices = torch.tensor([0, 2])
print(indices)
print(torch.index_select(x, 0, indices))
print(torch.index_select(x, 1, indices))
print(torch.index_select(x, 0, indices, out=torch.empty_like(x)))
print(torch.index_select(x, 1, indices, out=torch.empty_like(x)))