'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input = torch.randn(1, 3)
other = torch.randn(1, 3)
result = torch.fmax(input, other)
print(result)
result = torch.fmax(input, other, out=result)
print(result)