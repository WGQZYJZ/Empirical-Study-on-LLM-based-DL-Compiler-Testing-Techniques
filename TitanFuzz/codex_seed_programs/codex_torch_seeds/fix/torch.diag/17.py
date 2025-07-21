'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input = torch.rand(3, 3)
output = torch.diag(input)
print('input: ', input)
print('output: ', output)