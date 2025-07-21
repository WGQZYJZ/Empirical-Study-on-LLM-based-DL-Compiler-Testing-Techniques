'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
input = torch.rand(2, 3, 4)
print(input)
output = torch.expm1(input)
print(output)