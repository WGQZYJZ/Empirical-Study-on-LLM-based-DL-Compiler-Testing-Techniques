import torch
A = torch.randn(3, 3)
A = A.matmul(A.t())
eigen_values = torch.linalg.eigvalsh(A)