'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.tensor([[True, False], [False, False]])
print(x)
y = torch.all(x, dim=0)
print(y)
z = torch.all(x, dim=1)
print(z)
w = torch.all(x, dim=1, keepdim=True)
print(w)