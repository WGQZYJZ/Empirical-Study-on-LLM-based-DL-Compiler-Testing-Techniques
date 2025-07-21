'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
input = torch.randn(20, requires_grad=True)
print(input)
output = torch.square(input)
print(output)