'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
A = torch.randn(3, 3, requires_grad=True)
print(A)
B = torch.linalg.pinv(A)
print(B)
A.backward(torch.eye(3))
print(A.grad)