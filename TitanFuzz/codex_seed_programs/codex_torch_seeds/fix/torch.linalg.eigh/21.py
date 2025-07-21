"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.tensor([[2, 1], [1, 2]], dtype=torch.float64)
(eigenvalues, eigenvectors) = torch.linalg.eigh(A)
print('Eigenvalues are: ', eigenvalues)
print('Eigenvectors are: ', eigenvectors)