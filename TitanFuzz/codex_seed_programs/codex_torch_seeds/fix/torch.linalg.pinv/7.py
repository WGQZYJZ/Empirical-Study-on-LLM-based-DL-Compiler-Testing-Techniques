'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
A = torch.randn(3, 3, dtype=torch.float32)
print('A = \n', A)
A_pinv = torch.linalg.pinv(A)
print('A_pinv = \n', A_pinv)
print('A * A_pinv = \n', torch.matmul(A, A_pinv))
print('A_pinv * A = \n', torch.matmul(A_pinv, A))