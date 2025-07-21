'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
data = torch.randn(3, 4)
print(data)
print(torch.transpose(data, 0, 1))
print(torch.transpose(data, 0, 1).shape)