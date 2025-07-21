'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
input = torch.rand(2, 3)
mat2 = torch.rand(3, 2)
print(torch.mm(input, mat2))