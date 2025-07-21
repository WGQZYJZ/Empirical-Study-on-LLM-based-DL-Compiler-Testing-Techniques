'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
input = torch.tensor([0.2, 0.4, 0.6, 0.8, 1.0])
output = torch.special.ndtri(input)
print('input:', input)
print('output:', output)