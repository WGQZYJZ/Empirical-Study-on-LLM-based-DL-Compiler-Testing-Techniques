'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gather\ntorch.gather(input, dim, index, *, sparse_grad=False, out=None)\n'
import torch
input = torch.randn(3, 4)
index = torch.tensor([1, 1, 2])
print(input)
print(index)
print(torch.gather(input, 1, index.view((- 1), 1)))