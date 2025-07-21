'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.deg2rad\ntorch.deg2rad(input, *, out=None)\n'
import torch
input = torch.rand(3, 3)
print(input)
print(torch.deg2rad(input))
print(torch.deg2rad(input, out=input))
print(input)