'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagflat\ntorch.diagflat(input, offset=0)\n'
import torch
input = torch.randn(4, 4)
print(input)
output = torch.diagflat(input)
print(output)
output = torch.diagflat(input, offset=1)
print(output)
output = torch.diagflat(input, offset=(- 1))
print(output)