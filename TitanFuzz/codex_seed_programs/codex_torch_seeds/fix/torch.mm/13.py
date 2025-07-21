'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
input = torch.randn(2, 3)
mat2 = torch.randn(3, 2)
print(torch.mm(input, mat2))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, out=None)\n'
import torch
input = torch.randn(10, 3, 4)
mat2 = torch.randn(10, 4, 5)
print(torch.bmm(input, mat2).size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addmm\ntorch.addmm(input, mat1, mat2, *, beta=1, out=None)\n'
import torch
input = torch.randn(2, 3)
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 2)