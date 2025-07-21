'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print(x)
print(torch.log10(x))