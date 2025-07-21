'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pca_lowrank\ntorch.pca_lowrank(A, q=None, center=True, niter=2)\n'
import torch
import numpy as np
np.random.seed(0)
A = np.random.rand(100, 20)
A = torch.tensor(A, dtype=torch.float)
print(torch.pca_lowrank(A, q=None, center=True, niter=2))