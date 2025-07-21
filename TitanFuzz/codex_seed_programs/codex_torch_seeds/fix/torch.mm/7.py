'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
a = torch.rand(3, 4)
b = torch.rand(4, 5)
print(torch.mm(a, b))