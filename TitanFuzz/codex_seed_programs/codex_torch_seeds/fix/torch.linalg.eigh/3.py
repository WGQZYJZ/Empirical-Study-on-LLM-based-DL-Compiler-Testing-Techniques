"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
print('A = ', A)
(eigen_values, eigen_vectors) = torch.linalg.eigh(A)
print('eigen_values = ', eigen_values)
print('eigen_vectors = ', eigen_vectors)
print('A * eigen_vectors - eigen_values * eigen_vectors = ', (torch.mm(A, eigen_vectors) - torch.mm(eigen_vectors, torch.diag(eigen_values))))