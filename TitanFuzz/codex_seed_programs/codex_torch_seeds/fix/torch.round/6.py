'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
import torch
input = torch.randn(1, 3, 3)
print(input)
output = torch.round(input)
print(output)