'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
x = torch.tensor([[3, 4, 2], [5, 1, 7]])
print(x)
y = torch.sort(x, descending=True)
print(y)
z = torch.sort(x, descending=True, dim=1)
print(z)
a = torch.sort(x, descending=False, dim=1)
print(a)