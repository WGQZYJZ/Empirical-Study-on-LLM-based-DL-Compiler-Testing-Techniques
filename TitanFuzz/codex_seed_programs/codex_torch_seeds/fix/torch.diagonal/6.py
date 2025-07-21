'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagonal\ntorch.diagonal(input, offset=0, dim1=0, dim2=1)\n'
import torch
input = torch.arange(1, 17).view(4, 4)
print(input)
print(torch.diagonal(input))
print(torch.diagonal(input, offset=1))
print(torch.diagonal(input, offset=(- 1)))
print(torch.diagonal(input, offset=0, dim1=0, dim2=1))
print(torch.diagonal(input, offset=1, dim1=0, dim2=1))
print(torch.diagonal(input, offset=(- 1), dim1=0, dim2=1))
print(torch.diagonal(input, offset=0, dim1=1, dim2=0))
print(torch.diagonal(input, offset=1, dim1=1, dim2=0))
print