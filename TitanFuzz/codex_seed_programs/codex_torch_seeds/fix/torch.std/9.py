'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
print('input:', input)
print('torch.std(input, dim=0):', torch.std(input, dim=0))
print('torch.std(input, dim=1):', torch.std(input, dim=1))
print('torch.std(input, dim=2):', torch.std(input, dim=2))
print('torch.std(input, dim=(0, 1)):', torch.std(input, dim=(0, 1)))
print('torch.std(input, dim=(0, 2)):', torch.std(input, dim=(0, 2)))
print('torch.std(input, dim=(1, 2)):', torch.std(input, dim=(1, 2)))
print('torch.std(input, dim=(0, 1, 2)):', torch.std(input, dim=(0, 1, 2)))