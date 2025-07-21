'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0e\ntorch.special.i0e(input, *, out=None)\n'
import torch
import numpy as np
input = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
input = torch.from_numpy(input)
output = torch.special.i0e(input)
print('Input: ', input)
print('Output: ', output)