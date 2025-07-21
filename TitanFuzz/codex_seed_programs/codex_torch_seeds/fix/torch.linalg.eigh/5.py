"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
import numpy as np
A = np.random.randn(5, 5)
A = np.dot(A, A.T)
A = torch.from_numpy(A)
(eigval, eigvec) = torch.linalg.eigh(A)
print(eigval)
print(eigvec)