'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sin\ntorch.sin(input, *, out=None)\n'
import torch
input = torch.rand(4)
print(input)
output = torch.sin(input)
print(output)