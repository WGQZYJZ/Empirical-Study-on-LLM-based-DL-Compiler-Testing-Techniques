'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.sum\ntorch.sparse.sum(input, dim=None, dtype=None)\n'
import torch
indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([3, 4, 5], dtype=torch.float32)
sparse_tensor = torch.sparse_coo_tensor(indices, values, torch.Size([3, 3]))
sum_result = torch.sparse.sum(sparse_tensor, dim=0)
print(sum_result)
sum_result = torch.sparse.sum(sparse_tensor, dim=1)
print(sum_result)