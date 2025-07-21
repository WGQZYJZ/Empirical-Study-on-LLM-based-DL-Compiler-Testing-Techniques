'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse_coo_tensor\ntorch.sparse_coo_tensor(indices, values, size=None, *, dtype=None, device=None, requires_grad=False)\n'
import torch
indices = torch.tensor([[1, 0, 2], [0, 2, 1]])
values = torch.tensor([1, 2, 3])
torch.sparse_coo_tensor(indices, values, size=(3, 3))