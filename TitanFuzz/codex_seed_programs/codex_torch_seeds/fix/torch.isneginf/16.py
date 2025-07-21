'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input = torch.tensor([float('-inf'), float('inf'), float('nan'), float('-inf'), float('inf'), float('nan'), float('-inf'), float('inf'), float('nan')])
print('Input: ', input)
output = torch.isneginf(input)
print('Output: ', output)