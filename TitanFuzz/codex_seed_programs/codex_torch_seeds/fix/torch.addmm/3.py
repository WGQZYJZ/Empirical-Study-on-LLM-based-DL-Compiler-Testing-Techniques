'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addmm\ntorch.addmm(input, mat1, mat2, *, beta=1, alpha=1, out=None)\n'
import torch
inp = torch.randn(1, 10)
mat1 = torch.randn(10, 20)
mat2 = torch.randn(20, 10)
out = torch.addmm(inp, mat1, mat2)
print(out)