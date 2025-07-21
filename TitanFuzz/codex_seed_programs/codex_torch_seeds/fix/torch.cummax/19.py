'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
input = torch.rand(2, 3)
print('Input: ', input)
output = torch.cummax(input, dim=0)
print('Output: ', output)