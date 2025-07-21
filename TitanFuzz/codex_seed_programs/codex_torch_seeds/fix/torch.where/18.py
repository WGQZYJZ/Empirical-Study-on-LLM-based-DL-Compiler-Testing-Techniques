'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
x = torch.randn(3, 3)
print(x)
print(torch.where((x > 0), torch.tensor(1.0), torch.tensor(0.0)))