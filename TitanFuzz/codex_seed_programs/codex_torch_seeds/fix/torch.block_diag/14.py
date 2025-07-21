'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
import numpy as np
x = torch.rand(2, 3)
y = torch.rand(4, 3)
z = torch.rand(2, 4)
result = torch.block_diag(x, y, z)
print(result)
print(result.size())
print(result.dtype)