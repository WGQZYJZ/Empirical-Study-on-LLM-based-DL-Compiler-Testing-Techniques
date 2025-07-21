'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
d = torch.dist(x, y, p=2)
print(d)