'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input = torch.rand(2, 3)
print('Input: ', input)
print('Output: ', torch.triu(input))
print('Output: ', torch.triu(input, diagonal=1))
print('Output: ', torch.triu(input, diagonal=(- 1)))