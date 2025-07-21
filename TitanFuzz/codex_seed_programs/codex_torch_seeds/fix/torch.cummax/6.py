'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print(input)
output = torch.cummax(input, dim=0)
print(output)
output = torch.cummax(input, dim=1)
print(output)