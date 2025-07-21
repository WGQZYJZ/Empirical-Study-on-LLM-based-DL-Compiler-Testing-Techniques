'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
output = torch.diag(input)
print('Input: ', input)
print('Output: ', output)