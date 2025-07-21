'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
input = torch.randn(4, 3)
mat2 = torch.randn(3, 5)
output = torch.mm(input, mat2)
print(output)