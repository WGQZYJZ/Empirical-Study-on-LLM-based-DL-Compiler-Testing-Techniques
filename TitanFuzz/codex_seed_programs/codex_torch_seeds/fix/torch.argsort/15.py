'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
input = torch.randn(3, 4)
print(input)
print(torch.argsort(input, dim=(- 1), descending=True))