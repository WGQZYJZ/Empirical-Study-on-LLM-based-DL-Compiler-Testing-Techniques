'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pca_lowrank\ntorch.pca_lowrank(A, q=None, center=True, niter=2)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
A = torch.tensor(np.random.rand(10, 20))
print('Task 3: Call the API torch.pca_lowrank')
result = torch.pca_lowrank(A, q=None, center=True, niter=2)
print(result)