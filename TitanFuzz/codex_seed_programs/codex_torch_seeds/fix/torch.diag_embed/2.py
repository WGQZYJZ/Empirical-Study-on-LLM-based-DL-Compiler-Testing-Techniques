'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag_embed\ntorch.diag_embed(input, offset=0, dim1=-2, dim2=-1)\n'
import torch
input = torch.randn(3, 4, 5)
print(input)
print(torch.diag_embed(input))
print(torch.diag_embed(input, offset=1, dim1=1, dim2=2))