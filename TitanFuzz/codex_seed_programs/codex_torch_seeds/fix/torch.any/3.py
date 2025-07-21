'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print(x)
print(torch.any((x > 0.5), dim=1))