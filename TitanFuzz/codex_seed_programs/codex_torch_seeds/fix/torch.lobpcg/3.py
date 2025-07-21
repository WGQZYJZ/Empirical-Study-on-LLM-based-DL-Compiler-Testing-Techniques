'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lobpcg\ntorch.lobpcg(A, k=None, B=None, X=None, n=None, iK=None, niter=None, tol=None, largest=None, method=None, tracker=None, ortho_iparams=None, ortho_fparams=None, ortho_bparams=None)\n'
import torch
import numpy as np
n = 1000
d = 100
A = torch.rand(n, d, dtype=torch.float64)
A = torch.mm(A, A.transpose(0, 1))
(eigvals, eigvecs) = torch.lobpcg(A, k=10)
print(eigvals)
print(eigvecs)