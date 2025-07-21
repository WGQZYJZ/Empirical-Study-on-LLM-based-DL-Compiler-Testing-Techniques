'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.sum\ntorch.sparse.sum(input, dim=None, dtype=None)\n'
import torch
indices = torch.tensor([[0, 1], [1, 0]])
values = torch.tensor([1, 1], dtype=torch.float32)
sparse_mx = torch.sparse_coo_tensor(indices, values, [2, 2])
print(sparse_mx)
sum_sparse_mx = torch.sparse.sum(sparse_mx, dim=0)
print(sum_sparse_mx)