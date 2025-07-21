'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse_coo_tensor\ntorch.sparse_coo_tensor(indices, values, size=None, *, dtype=None, device=None, requires_grad=False)\n'
import torch
import numpy as np
values = torch.tensor([1, 2, 3, 4, 5, 6], dtype=torch.float32)
indices = torch.tensor([[0, 1, 1, 2, 2, 3], [0, 0, 1, 0, 1, 2]], dtype=torch.int64)
size = torch.Size([4, 3])
output = torch.sparse_coo_tensor(indices, values, size)
print('output: ', output)
output = torch.sparse_coo_tensor(indices, values, size, device='cuda')
print('output: ', output)