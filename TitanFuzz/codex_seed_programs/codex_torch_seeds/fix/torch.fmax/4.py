'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.fmax(input, other)
print(input)
print(other)
print(output)