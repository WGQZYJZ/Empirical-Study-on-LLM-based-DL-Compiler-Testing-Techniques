'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addmm\ntorch.addmm(input, mat1, mat2, *, beta=1, alpha=1, out=None)\n'
import torch
input = torch.randn(20, 20)
mat1 = torch.randn(20, 30)
mat2 = torch.randn(30, 20)
torch.addmm(input, mat1, mat2)
out = torch.randn(20, 20)
torch.addmm(input, mat1, mat2, out=out)