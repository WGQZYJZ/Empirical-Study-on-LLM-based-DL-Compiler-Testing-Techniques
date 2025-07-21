'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
import numpy as np
input = torch.tensor([(- 1), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
other = torch.tensor([(- 1), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
output = torch.special.zeta(input, other)
print(output)