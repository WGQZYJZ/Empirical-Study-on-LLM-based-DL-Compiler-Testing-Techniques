'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.copysign\ntorch.copysign(input, other, *, out=None)\n'
import torch
import numpy as np
input = np.array([(- 1), (- 2), (- 3), (- 4), (- 5)])
other = np.array([1, 2, 3, 4, 5])
print('Input: ', input)
print('Other: ', other)
print('Output: ', torch.copysign(torch.from_numpy(input), torch.from_numpy(other)))