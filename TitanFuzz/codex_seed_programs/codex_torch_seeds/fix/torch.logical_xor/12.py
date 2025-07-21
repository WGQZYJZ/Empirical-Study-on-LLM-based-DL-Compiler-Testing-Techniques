'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
x = torch.tensor([True, False, True, False])
y = torch.tensor([True, True, False, False])
print(torch.logical_xor(x, y))