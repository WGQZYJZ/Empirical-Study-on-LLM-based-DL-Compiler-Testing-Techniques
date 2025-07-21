'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ne\ntorch.ne(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 2, 3], [4, 5, 6]])
out = torch.ne(input, other)
print('input = ', input)
print('other = ', other)
print('out = ', out)