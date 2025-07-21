'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lobpcg\ntorch.lobpcg(A, k=None, B=None, X=None, n=None, iK=None, niter=None, tol=None, largest=None, method=None, tracker=None, ortho_iparams=None, ortho_fparams=None, ortho_bparams=None)\n'
import torch
A = torch.randn(100, 100)
A = torch.mm(A, A.t())
(eigvals, eigvecs) = torch.lobpcg(A, k=10)
print(eigvals)
print(eigvecs)