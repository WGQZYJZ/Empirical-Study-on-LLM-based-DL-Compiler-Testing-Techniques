'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input = torch.Tensor([(- 1), float('-inf'), 0, float('inf'), 1])
print(torch.isneginf(input))