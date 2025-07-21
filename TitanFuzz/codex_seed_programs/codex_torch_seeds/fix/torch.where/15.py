'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
x = torch.randn(5, 5)
y = torch.randn(5, 5)
z = torch.where((x > 0), x, y)
print(x)
print(y)
print(z)