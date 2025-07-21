'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input = torch.tensor([(- float('inf')), (- float('inf')), float('inf'), float('inf'), float('nan'), float('nan')])
print(input)
print(torch.isneginf(input))