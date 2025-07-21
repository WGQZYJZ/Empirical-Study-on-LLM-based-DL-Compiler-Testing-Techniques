'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
input = torch.randn(1, 3, 3)
print(input)
output = torch.arctan(input)
print(output)