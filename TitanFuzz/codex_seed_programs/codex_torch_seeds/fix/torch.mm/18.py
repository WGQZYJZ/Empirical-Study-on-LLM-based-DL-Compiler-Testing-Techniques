'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
mat2 = torch.randn(4, 5)
torch.mm(input, mat2)
out = torch.randn(3, 5)
torch.mm(input, mat2, out=out)
out