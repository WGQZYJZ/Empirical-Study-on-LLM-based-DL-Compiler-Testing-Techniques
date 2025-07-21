'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(3, 4)
input[1][1] = np.nan
print(input)
result = torch.nanmedian(input)
print(result)