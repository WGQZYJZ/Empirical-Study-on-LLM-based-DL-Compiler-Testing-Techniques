'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.sum\ntorch.sparse.sum(input, dim=None, dtype=None)\n'
import torch
indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([1, 2, 3], dtype=torch.float32)
sparse_tensor = torch.sparse_coo_tensor(indices, values, size=(3, 3))
print(torch.sparse.sum(sparse_tensor, dim=0))
print(torch.sparse.sum(sparse_tensor, dim=1))
print(torch.sparse.sum(sparse_tensor))