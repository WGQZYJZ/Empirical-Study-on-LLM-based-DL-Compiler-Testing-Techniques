'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input = torch.tensor([1, (- 1), float('inf'), float('-inf'), float('nan')])
print('Input: ', input)
print('Output: ', torch.isneginf(input))