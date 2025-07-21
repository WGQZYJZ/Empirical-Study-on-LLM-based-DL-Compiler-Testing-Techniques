'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
import numpy as np
input = np.array([1, np.nan, np.inf])
input = torch.tensor(input)
output = torch.isfinite(input)
print('Output: ', output)