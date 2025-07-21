'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pca_lowrank\ntorch.pca_lowrank(A, q=None, center=True, niter=2)\n'
import torch
A = torch.randn(10, 5)
torch.pca_lowrank(A, q=None, center=True, niter=2)