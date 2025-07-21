'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
A = torch.Tensor([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
L = torch.linalg.cholesky(A)
print('The lower triangular matrix L is: \n', L)
print('The result of L*L.t() is: \n', torch.mm(L, L.t()))