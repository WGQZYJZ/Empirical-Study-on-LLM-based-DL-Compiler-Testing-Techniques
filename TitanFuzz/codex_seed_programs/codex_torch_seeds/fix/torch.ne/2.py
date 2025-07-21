'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ne\ntorch.ne(input, other, *, out=None)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[1, 2], [3, 4]])
c = torch.ne(a, b)
print(c)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[1, 2], [3, 4]])
c = torch.eq(a, b)