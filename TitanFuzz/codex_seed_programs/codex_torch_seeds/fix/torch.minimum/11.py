'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.minimum\ntorch.minimum(input, other, *, out=None)\n'
import torch
a = torch.randn(2, 3)
b = torch.randn(2, 3)
print(torch.minimum(a, b))
print(torch.min(a))
print(torch.min(a, 0))
print(torch.min(a, 1))