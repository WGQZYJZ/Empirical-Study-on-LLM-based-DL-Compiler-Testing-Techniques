'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag_embed\ntorch.diag_embed(input, offset=0, dim1=-2, dim2=-1)\n'
import torch
input = torch.randn(2, 3, 4)
print('input = ', input)
output = torch.diag_embed(input)
print('output = ', output)
output = torch.diag_embed(input, offset=1)
print('output = ', output)
output = torch.diag_embed(input, offset=1, dim1=1, dim2=2)
print('output = ', output)