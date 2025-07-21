'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagonal\ntorch.diagonal(input, offset=0, dim1=0, dim2=1)\n'
import torch
x = torch.arange(0, 6).view(2, 3)
print(x)
print(torch.diagonal(x))
print(torch.diagonal(x, offset=1))
print(torch.diagonal(x, offset=(- 1)))
print(torch.diagonal(x, offset=0, dim1=0, dim2=1))
print(torch.diagonal(x, offset=1, dim1=0, dim2=1))
print(torch.diagonal(x, offset=(- 1), dim1=0, dim2=1))