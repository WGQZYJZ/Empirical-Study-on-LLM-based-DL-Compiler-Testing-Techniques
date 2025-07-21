'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 4)
other = torch.randn(3, 4)
print(torch.fmax(input, other))