'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagonal\ntorch.diagonal(input, offset=0, dim1=0, dim2=1)\n'
import torch
input = torch.arange(1, 9).view(2, 4)
print(input)
output = torch.diagonal(input, offset=0, dim1=0, dim2=1)
print(output)