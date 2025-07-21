'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(3, 4)
print('input = ', input)
print('Task 3: Call the API torch.argsort')
print('torch.argsort(input, dim=-1, descending=False)')
print('torch.argsort(input, dim=0, descending=False)')
print('torch.argsort(input, dim=1, descending=False)')
print('torch.argsort(input, dim=-1, descending=True)')
print('torch.argsort(input, dim=0, descending=True)')
print('torch.argsort(input, dim=1, descending=True)')
print('torch.argsort(input, dim=-1, descending=False) = ', torch.argsort(input, dim=(- 1), descending=False))