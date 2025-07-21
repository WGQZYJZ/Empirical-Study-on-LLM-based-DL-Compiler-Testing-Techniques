'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
A = torch.randn(2, 2)
print(A)
print(torch.linalg.cond(A))
print(torch.linalg.cond((A.t() @ A)))
print(torch.linalg.cond((A @ A.t())))
print(torch.linalg.cond(((A @ A.t()) + torch.eye(2))))