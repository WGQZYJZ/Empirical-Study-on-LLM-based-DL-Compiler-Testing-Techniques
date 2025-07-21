'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
input = torch.randn(5, 3)
print(input)
output = torch.sqrt(input)
print(output)