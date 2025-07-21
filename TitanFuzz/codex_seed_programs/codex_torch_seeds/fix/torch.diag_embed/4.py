'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag_embed\ntorch.diag_embed(input, offset=0, dim1=-2, dim2=-1)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(torch.diag_embed(input))
print(torch.diag_embed(input, offset=1))
print(torch.diag_embed(input, offset=(- 2)))
print(torch.diag_embed(input, offset=1, dim1=0, dim2=1))
print(torch.diag_embed(input, offset=1, dim1=1, dim2=0))
print(torch.diag_embed(input, offset=1, dim1=1, dim2=2))
print(torch.diag_embed(input, offset=1, dim1=2, dim2=1))
'\nTask 4: Call the API torch.diag_embed\ntorch.diag_embed(input, offset=0, dim1=-2, dim2=-1)\n'