'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 5)
other = torch.randn(3, 5)
output = torch.fmax(input, other)
print(output)