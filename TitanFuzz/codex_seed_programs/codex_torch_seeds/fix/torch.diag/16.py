'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input data: ', input)
print('Diagonal elements: ', torch.diag(input))