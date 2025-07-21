'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 2)
output = torch.mm(mat1, mat2)
print(output)
output = torch.mm(mat1, mat2, out=torch.empty(2, 2))
print(output)