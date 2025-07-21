'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inner\ntorch.inner(input, other, *, out=None)\n'
import torch
x = torch.randn(3, 4)
y = torch.randn(4)
print(torch.inner(x, y))