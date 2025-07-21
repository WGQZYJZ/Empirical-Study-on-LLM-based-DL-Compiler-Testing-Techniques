'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_not\ntorch.logical_not(input, *, out=None)\n'
import torch
x = torch.tensor([False, True, True, False])
print(x)
y = torch.logical_not(x)
print(y)
z = torch.logical_not(x, out=x)
print(z)
w = x.logical_not()
print(w)