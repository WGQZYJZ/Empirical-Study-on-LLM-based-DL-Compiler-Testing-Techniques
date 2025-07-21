'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(input)
output = torch.abs(input)
print(output)
torch.abs_(input)
print(input)