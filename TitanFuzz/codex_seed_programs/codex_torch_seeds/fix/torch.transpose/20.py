'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
a = torch.arange(0, 12)
a = a.view(3, 4)
print(a)
b = torch.transpose(a, 0, 1)
print(b)