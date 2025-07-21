'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input = torch.Tensor([(- float('inf')), float('inf'), float('-inf')])
print(torch.isneginf(input))