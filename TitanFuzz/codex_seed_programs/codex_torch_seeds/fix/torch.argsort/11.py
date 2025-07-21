'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
x = torch.rand(2, 3)
print(x)
print(torch.argsort(x, dim=(- 1), descending=False))
print(torch.argsort(x, dim=(- 1), descending=True))