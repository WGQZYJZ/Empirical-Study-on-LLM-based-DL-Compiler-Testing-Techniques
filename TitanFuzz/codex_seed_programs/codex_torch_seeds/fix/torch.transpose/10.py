'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
a = torch.randn(2, 3)
print(a)
print(a.t())
print(torch.transpose(a, 0, 1))