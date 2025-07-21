'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lobpcg\ntorch.lobpcg(A, k=None, B=None, X=None, n=None, iK=None, niter=None, tol=None, largest=None, method=None, tracker=None, ortho_iparams=None, ortho_fparams=None, ortho_bparams=None)\n'
import torch
import numpy as np
A = np.random.rand(100, 100)
A = torch.from_numpy(A)
torch.lobpcg(A)