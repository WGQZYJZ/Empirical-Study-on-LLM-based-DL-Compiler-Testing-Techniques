'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag_embed\ntorch.diag_embed(input, offset=0, dim1=-2, dim2=-1)\n'
import torch
input = torch.arange(1, 7).view(2, 3)
output = torch.diag_embed(input, offset=0, dim1=(- 2), dim2=(- 1))
print('input:', input)
print('output:', output)