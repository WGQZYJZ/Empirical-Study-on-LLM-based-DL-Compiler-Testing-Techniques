'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
A = torch.arange(6).view(2, 3)
B = torch.arange(6).view(3, 2)
torch.einsum('ij,jk->ik', (A, B))