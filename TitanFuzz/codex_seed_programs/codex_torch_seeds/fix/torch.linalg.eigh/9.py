"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
import numpy as np
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
(eigen_val, eigen_vec) = torch.linalg.eigh(A)
print('eigen values:', eigen_val)
print('eigen vectors:', eigen_vec)