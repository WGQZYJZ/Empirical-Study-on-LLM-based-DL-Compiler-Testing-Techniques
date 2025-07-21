'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
input = torch.randn(10, 10)
output = torch.arctan(input)
print(output)