"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.rand(2, 2)
A_t = A.t()
A_sym = torch.mm(A_t, A)
(e, v) = torch.linalg.eigh(A_sym)
print(e)
print(v)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eig\ntorch.linalg.eig(A, UPLO='L', *, out=None)\n"
import torch
A = torch.rand(2, 2)
A_t = A.t()
A_sym = torch.mm(A_t, A)
(e, v) = torch.linalg.eig(A_sym)
print(e)
print(v)