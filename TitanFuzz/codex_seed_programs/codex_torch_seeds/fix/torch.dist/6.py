'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
print(x)
print(y)
print(torch.dist(x, y, p=2))