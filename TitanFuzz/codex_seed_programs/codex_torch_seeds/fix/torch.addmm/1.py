'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addmm\ntorch.addmm(input, mat1, mat2, *, beta=1, alpha=1, out=None)\n'
import torch
mat1 = torch.ones(10, 10)
mat2 = torch.ones(10, 10)
mat3 = torch.ones(10, 10)
torch.addmm(mat1, mat2, mat3)