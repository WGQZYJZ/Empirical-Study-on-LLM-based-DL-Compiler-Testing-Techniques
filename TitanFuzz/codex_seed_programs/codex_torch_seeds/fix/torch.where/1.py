'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
x = torch.randn(3, 3)
y = torch.randn(3, 3)
condition = torch.randn(3, 3)
z = torch.where((condition < 0), x, y)
print(z)