'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
input = torch.tensor([float('inf'), float('-inf'), float('nan'), float('-nan')])
print('Input: ', input)
output = torch.isposinf(input)
print('Output: ', output)