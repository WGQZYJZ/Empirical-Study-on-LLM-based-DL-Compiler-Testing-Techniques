'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
input = torch.randn(4)
print(input)
print(torch.rad2deg(input))