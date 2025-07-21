'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chain_matmul\ntorch.chain_matmul(*matrices, out=None)\n'
import torch
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(A)
B = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(B)
C = torch.chain_matmul(A, B)
print(C)
D = torch.chain_matmul(A, B, A)
print(D)
E = torch.chain_matmul(A, B, A, B)
print(E)
F = torch.chain_matmul(A, B, A, B, A)
print(F)