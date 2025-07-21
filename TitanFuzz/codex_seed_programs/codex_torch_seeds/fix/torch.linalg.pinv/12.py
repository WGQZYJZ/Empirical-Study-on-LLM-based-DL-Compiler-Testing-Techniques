'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
import math
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
print('A = ', A)
A_inv = torch.linalg.pinv(A)
print('A_inv = ', A_inv)
A_dot_A_inv = torch.mm(A, A_inv)
print('A_dot_A_inv = ', A_dot_A_inv)
A_inv_dot_A = torch.mm(A_inv, A)
print('A_inv_dot_A = ', A_inv_dot_A)