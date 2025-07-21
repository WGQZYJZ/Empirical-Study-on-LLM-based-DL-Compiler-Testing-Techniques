'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse_coo_tensor\ntorch.sparse_coo_tensor(indices, values, size=None, *, dtype=None, device=None, requires_grad=False)\n'
import torch
indices = torch.tensor([[0, 1], [1, 0]])
values = torch.tensor([1, 1])
size = torch.Size([2, 2])
output = torch.sparse_coo_tensor(indices, values, size)
print('output = \n', output)