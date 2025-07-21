'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.sum\ntorch.sparse.sum(input, dim=None, dtype=None)\n'
import torch
indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([3, 4, 5], dtype=torch.float32)
size = torch.Size([3, 3])
input = torch.sparse_coo_tensor(indices, values, size)
print('input: ', input)
output = torch.sparse.sum(input, dim=None, dtype=None)
print('output: ', output)