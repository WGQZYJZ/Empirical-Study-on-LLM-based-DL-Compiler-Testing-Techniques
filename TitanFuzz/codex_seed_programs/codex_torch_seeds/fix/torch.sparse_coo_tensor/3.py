'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse_coo_tensor\ntorch.sparse_coo_tensor(indices, values, size=None, *, dtype=None, device=None, requires_grad=False)\n'
import torch
indices = torch.LongTensor([[0, 1, 1], [2, 0, 2]])
values = torch.FloatTensor([3, 4, 5])
size = torch.Size([3, 3])
res = torch.sparse_coo_tensor(indices, values, size)
print(res)