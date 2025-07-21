"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
(w, v) = torch.linalg.eigh(A)
print(f'Eigenvalues: {w}')
print(f'Eigenvectors: {v}')
A_inv = torch.inverse(A)
print(f'Inverse of A: {A_inv}')
I = torch.matmul(A, A_inv)
print(f'A * A_inv: {I}')