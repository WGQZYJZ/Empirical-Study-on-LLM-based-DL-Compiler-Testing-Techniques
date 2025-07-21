'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagonal\ntorch.diagonal(input, offset=0, dim1=0, dim2=1)\n'
import torch
tensor = torch.randn(3, 3)
print(tensor)
print(torch.diagonal(tensor))
print(torch.diagonal(tensor, offset=1))
print(torch.diagonal(tensor, offset=(- 1)))
tensor = torch.randn(3, 3, 3)
print(tensor)
print(torch.diagonal(tensor, dim1=1, dim2=2))