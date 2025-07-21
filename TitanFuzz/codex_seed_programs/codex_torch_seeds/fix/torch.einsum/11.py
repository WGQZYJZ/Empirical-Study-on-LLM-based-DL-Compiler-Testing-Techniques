'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
A = torch.rand(3, 5)
B = torch.rand(5, 3)
torch.einsum('ij, jk -> ik', A, B)
torch.einsum('ij, jk -> ik', A, B)
torch.einsum('ij, jk -> ik', A, B)
torch.einsum('ij, jk -> ik', A, B)
torch.einsum('ij, jk -> ik', A, B)