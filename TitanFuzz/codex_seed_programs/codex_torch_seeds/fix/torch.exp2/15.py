'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
x = torch.randn(2, 2)
print(x)
print(torch.exp2(x))