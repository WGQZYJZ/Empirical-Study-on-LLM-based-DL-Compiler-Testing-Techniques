"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
(eig_val, eig_vec) = torch.linalg.eigh(A)
print('Eigen values: ', eig_val)
print('Eigen vectors: ', eig_vec)