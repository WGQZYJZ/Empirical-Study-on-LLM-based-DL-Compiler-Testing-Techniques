'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input = torch.tensor([0.0, (- float('inf')), float('inf')])
output = torch.isneginf(input)
print('input:', input)
print('output:', output)