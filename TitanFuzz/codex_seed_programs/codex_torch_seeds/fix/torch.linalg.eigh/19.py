"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
print(A)
(eigen_values, eigen_vectors) = torch.linalg.eigh(A)
print(eigen_values)
print(eigen_vectors)
print(torch.matmul(A, eigen_vectors))
print((eigen_values * eigen_vectors))
print(torch.allclose(torch.matmul(A, eigen_vectors), (eigen_values * eigen_vectors)))