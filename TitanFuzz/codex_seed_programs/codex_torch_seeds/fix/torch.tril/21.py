'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
input = torch.rand(3, 3)
print('Input data: ', input)
output = torch.tril(input)
print('Output data: ', output)