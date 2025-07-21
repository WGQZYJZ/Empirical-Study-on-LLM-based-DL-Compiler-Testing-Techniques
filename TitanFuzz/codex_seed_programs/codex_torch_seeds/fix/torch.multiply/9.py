'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
input = torch.rand(2, 3)
other = torch.rand(2, 3)
output = torch.multiply(input, other)
print(output)