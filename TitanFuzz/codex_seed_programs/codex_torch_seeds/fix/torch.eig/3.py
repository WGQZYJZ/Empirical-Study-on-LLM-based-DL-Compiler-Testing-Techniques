'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
A = torch.randn(3, 3, dtype=torch.float64)
(eigenvalues, eigenvectors) = torch.eig(A, True)
print(f'The eigenvalues of A are: {eigenvalues}')
print(f'The eigenvectors of A are: {eigenvectors}')