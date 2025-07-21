'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan2\ntorch.atan2(input, other, *, out=None)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
print(x)
print(y)
print(torch.atan2(x, y))