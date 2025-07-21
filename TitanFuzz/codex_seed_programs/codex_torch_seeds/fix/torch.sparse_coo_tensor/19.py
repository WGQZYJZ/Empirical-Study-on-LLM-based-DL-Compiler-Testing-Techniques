'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse_coo_tensor\ntorch.sparse_coo_tensor(indices, values, size=None, *, dtype=None, device=None, requires_grad=False)\n'
import torch
indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([3, 4, 5], dtype=torch.float32)
print(indices)
print(values)
x = torch.sparse_coo_tensor(indices, values, size=(3, 3))
print(x)
x = torch.sparse_coo_tensor(indices, values, size=(3, 3), dtype=torch.float64)
print(x)
indices = torch.tensor([[0, 1, 1], [2, 0, 2]], dtype=torch.long)
values = torch.tensor([3, 4, 5], dtype=torch.float32)
print(indices)