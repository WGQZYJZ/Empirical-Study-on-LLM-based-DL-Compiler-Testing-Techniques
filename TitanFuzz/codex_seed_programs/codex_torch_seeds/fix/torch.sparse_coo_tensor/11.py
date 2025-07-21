'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse_coo_tensor\ntorch.sparse_coo_tensor(indices, values, size=None, *, dtype=None, device=None, requires_grad=False)\n'
import torch
import numpy as np
indices = np.array([[0, 1, 1], [2, 0, 2]])
values = np.array([1, 2, 3])
torch_sparse_tensor = torch.sparse_coo_tensor(indices, values)
print(torch_sparse_tensor)