'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
x = torch.randn(2, 3, 4)
y = torch.randn(3, 4, 5)
z = torch.randn(4, 5, 6)
result = torch.einsum('ijk,jkl,klm->ilm', x, y, z)