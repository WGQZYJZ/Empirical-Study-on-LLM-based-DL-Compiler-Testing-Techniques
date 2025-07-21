'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input = torch.randn(4, 4)
other = torch.randn(4, 4)
output = torch.fmax(input, other)
print(input)
print(other)
print(output)