"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.Tensor([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
(eig_val, eig_vec) = torch.linalg.eigh(A)
print('Eigenvalues:', eig_val)
print('Eigenvectors:', eig_vec)