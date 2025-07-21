'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input = torch.tensor([(- float('inf')), (- 1), 0, 1, float('inf')])
output = torch.isneginf(input)
print(output)