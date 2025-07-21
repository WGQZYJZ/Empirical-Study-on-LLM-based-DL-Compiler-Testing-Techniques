'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.tensor([[True, False, False], [False, False, False]])
print(x)
y = torch.any(x)
print(y)
y = torch.any(x, dim=0)
print(y)
y = torch.any(x, dim=1)
print(y)
y = torch.any(x, dim=1, keepdim=True)
print(y)