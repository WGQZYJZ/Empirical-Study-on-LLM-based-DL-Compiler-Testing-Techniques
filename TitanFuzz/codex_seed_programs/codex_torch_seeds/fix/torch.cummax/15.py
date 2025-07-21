'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(input)
print(torch.cummax(input, dim=0))
print(torch.cummax(input, dim=1))