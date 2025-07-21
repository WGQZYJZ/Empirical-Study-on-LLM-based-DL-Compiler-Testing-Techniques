'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
input = torch.randn(1, 3)
mat2 = torch.randn(3, 3)
print(torch.mm(input, mat2))