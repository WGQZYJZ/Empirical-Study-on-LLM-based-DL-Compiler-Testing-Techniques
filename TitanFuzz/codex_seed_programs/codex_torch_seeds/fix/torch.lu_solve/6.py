'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lu_solve\ntorch.lu_solve(b, LU_data, LU_pivots, *, out=None)\n'
import torch
import numpy as np
np.random.seed(1)
A = np.random.randint(low=0, high=10, size=(3, 3))
A = torch.from_numpy(A).float()
b = np.random.randint(low=0, high=10, size=(3, 1))
b = torch.from_numpy(b).float()
(LU_data, LU_pivots) = torch.lu(A)
x = torch.lu_solve(b, LU_data, LU_pivots)
print(x)