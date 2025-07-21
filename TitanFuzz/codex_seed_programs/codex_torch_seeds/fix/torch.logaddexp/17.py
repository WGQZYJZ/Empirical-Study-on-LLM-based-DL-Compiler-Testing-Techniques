'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logaddexp\ntorch.logaddexp(input, other, *, out=None)\n'
import torch
x = torch.randn(5)
y = torch.randn(5)
z = torch.logaddexp(x, y)
print(z)