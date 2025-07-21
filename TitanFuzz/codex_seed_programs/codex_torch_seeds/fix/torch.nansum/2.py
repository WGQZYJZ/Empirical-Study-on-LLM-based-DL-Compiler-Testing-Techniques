'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nansum\ntorch.nansum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
import numpy as np
input = np.array([[1, np.nan, 2], [2, 3, np.nan]])
input = torch.from_numpy(input)
print(torch.nansum(input, dim=1))
print(torch.nansum(input, dim=1, keepdim=True))
print(torch.nansum(input, dim=1, keepdim=True, dtype=torch.float64))