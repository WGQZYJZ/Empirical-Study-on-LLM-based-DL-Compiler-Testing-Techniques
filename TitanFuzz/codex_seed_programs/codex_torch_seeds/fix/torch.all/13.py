'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.tensor([[True, False], [False, False]])
y = torch.all(x, dim=1)
print(y)