'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
A = torch.randn(3, 3)
A_pinv = torch.linalg.pinv(A)
print('A:\n', A)
print('A_pinv:\n', A_pinv)
torch.allclose(torch.mm(A, A_pinv), torch.eye(3))
torch.allclose(torch.mm(A_pinv, A), torch.eye(3))