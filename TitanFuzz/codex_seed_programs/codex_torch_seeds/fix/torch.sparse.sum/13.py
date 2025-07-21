'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.sum\ntorch.sparse.sum(input, dim=None, dtype=None)\n'
import torch
input = torch.sparse_coo_tensor(torch.tensor([[0, 1, 1], [2, 0, 2]]), torch.tensor([1, 2, 3]), torch.Size([3, 3]))
output = torch.sparse.sum(input, dim=None, dtype=None)