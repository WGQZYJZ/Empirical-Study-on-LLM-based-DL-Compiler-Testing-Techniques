"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
A = torch.matmul(A, A.t())
(eigen_values, eigen_vectors) = torch.linalg.eigh(A)
print('eigen values: ', eigen_values)
print('eigen vectors: ', eigen_vectors)