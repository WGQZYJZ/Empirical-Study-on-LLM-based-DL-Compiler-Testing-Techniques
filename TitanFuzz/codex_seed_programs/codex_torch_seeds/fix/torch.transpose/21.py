'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
x = torch.rand(3, 4)
print(x)
print('\n')
print(torch.transpose(x, 0, 1))