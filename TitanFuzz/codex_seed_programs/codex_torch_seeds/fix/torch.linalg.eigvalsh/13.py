"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
A_sym = ((A + A.t()) / 2)
eigvals = torch.linalg.eigvalsh(A_sym)
print('eigenvalues of A_sym: ', eigvals)
(eigvals_sorted, perm) = torch.sort(eigvals)
print('eigenvalues of A_sym sorted: ', eigvals_sorted)
print('permutation: ', perm)
A_sym_sorted = A_sym[perm, :][:, perm]
print('A_sym sorted: ', A_sym_sorted)