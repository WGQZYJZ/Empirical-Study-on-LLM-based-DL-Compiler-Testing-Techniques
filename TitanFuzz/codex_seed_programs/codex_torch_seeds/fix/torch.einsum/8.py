'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
N = 3
M = 4
K = 5
A = torch.randn(N, M)
B = torch.randn(M, K)
C = torch.einsum('ij,jk->ik', A, B)
print(C.shape)