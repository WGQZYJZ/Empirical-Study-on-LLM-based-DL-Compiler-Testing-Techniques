'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.angle\ntorch.angle(input, *, out=None)\n'
import torch
input = torch.rand(2, 3)
print(input)
print(torch.angle(input))