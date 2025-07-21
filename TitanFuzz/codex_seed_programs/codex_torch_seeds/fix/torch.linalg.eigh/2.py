"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.tensor([[1.0, 2.0, 3.0], [2.0, (- 1.0), 4.0], [3.0, 4.0, (- 2.0)]])
(eig_val, eig_vec) = torch.linalg.eigh(A)
print('eig_val = ', eig_val)
print('eig_vec = ', eig_vec)
print('Verify that eig_val[i] is the eigenvalue of eig_vec[:, i]')
print('eig_val[0] = ', eig_val[0])
print('torch.matmul(A, eig_vec[:, 0]) = ', torch.matmul(A, eig_vec[:, 0]))