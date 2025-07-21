'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.normal\ntorch.normal(mean, std, size, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print(x)
x = torch.normal(mean=0.0, std=1.0, size=(3, 3))
print(x)