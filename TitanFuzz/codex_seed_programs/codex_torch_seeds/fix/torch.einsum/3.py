'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6]])
B = torch.tensor([[7, 8, 9], [10, 11, 12]])
C = torch.einsum('ik,jk->ijk', A, B)
print(C)