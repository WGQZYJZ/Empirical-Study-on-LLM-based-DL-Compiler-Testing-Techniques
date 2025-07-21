'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan\ntorch.atan(input, *, out=None)\n'
import torch
input = torch.randn(1, 3, 4)
output = torch.atan(input)
print(output)