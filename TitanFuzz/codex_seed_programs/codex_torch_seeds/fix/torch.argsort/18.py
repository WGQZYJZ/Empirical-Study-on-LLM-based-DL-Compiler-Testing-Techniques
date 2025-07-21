'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
input = torch.rand(5, 3)
print(input)
print(torch.argsort(input, dim=(- 1), descending=False))
print(torch.argsort(input, dim=(- 1), descending=True))
print(torch.argsort(input, dim=0, descending=True))
print(torch.argsort(input, dim=0, descending=False))
input = torch.rand(3, 5)
print(input)
print(torch.argsort(input, dim=0, descending=False))
print(torch.argsort(input, dim=0, descending=True))
print(torch.argsort(input, dim=1, descending=False))
print(torch.argsort(input, dim=1, descending=True))