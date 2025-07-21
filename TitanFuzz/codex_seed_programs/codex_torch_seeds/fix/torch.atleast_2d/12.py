'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_2d\ntorch.atleast_2d(*tensors)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 2])
print(torch.atleast_2d(x))
print(torch.atleast_2d(y))
print(torch.atleast_2d(x, y))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(seq, dim=0, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 2])
print(torch.cat((x, y)))