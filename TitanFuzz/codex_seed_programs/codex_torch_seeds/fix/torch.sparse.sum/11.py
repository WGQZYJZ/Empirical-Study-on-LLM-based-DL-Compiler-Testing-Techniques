'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.sum\ntorch.sparse.sum(input, dim=None, dtype=None)\n'
import torch
i = torch.tensor([[0, 1, 1], [2, 0, 2]])
v = torch.tensor([3, 4, 5], dtype=torch.float32)
input = torch.sparse.FloatTensor(i, v, torch.Size([3, 3]))
print('input = ', input)
output = torch.sparse.sum(input)
print('output = ', output)
output = torch.sparse.sum(input, dim=0)
print('output = ', output)
output = torch.sparse.sum(input, dim=1)
print('output = ', output)
output = torch.sparse.sum(input, dtype=torch.int64)