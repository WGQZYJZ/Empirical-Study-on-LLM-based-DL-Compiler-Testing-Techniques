'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
import numpy as np
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
x = torch.randn(3, 4, 5)
y = torch.randn(4, 5)
z = torch.randn(5, 6)
'\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
print(torch.einsum('ijk,jk->i', x, y))
print(torch.einsum('ij,jk->ik', y, z))