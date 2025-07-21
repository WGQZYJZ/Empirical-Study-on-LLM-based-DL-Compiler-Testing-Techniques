'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
A = torch.randn(3, 3, requires_grad=True)
pinv_A = torch.linalg.pinv(A)
print(pinv_A)
'\nTask 4: Compute the inverse of a matrix\ntorch.inverse(input, *, out=None)\n'
A = torch.randn(3, 3, requires_grad=True)
inv_A = torch.inverse(A)
print(inv_A)
'\nTask 5: Compute the eigenvalues and eigenvectors of a square matrix\ntorch.eig(a, eigenvectors=False, *, out=None)\n'
A = torch.randn(3, 3, requires_grad=True)
eig_A = torch.eig(A)