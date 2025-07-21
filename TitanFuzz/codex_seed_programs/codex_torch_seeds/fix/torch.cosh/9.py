'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cosh\ntorch.cosh(input, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3])
print(x)
out = torch.cosh(x)
print(out)