"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
A = A.matmul(A.t())
print(A)
eigen_values = torch.linalg.eigvalsh(A)
print(eigen_values)