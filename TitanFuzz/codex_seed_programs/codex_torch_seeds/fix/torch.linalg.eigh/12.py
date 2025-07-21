"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(2, 2)
(eigen_values, eigen_vectors) = torch.linalg.eigh(A)
print('Eigen values: ', eigen_values)
print('Eigen vectors: ', eigen_vectors)