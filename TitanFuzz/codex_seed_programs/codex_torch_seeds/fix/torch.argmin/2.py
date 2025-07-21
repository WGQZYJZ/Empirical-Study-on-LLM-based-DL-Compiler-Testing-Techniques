'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
a = torch.randn(4, 4)
print(a)
print(torch.argmin(a, dim=1))
print(torch.argmin(a, dim=1, keepdim=True))