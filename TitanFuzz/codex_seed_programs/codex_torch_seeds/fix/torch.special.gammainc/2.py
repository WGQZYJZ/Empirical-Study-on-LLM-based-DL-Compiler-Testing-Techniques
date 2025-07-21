'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammainc\ntorch.special.gammainc(input, other, *, out=None)\n'
import torch
x = torch.rand(1)
a = torch.rand(1)
y = torch.special.gammainc(x, a)
print(y)