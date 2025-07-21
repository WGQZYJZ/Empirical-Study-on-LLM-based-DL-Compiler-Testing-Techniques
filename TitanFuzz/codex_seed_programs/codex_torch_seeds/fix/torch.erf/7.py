'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erf\ntorch.erf(input, *, out=None)\n'
import torch
import numpy as np
input = np.random.randn(2, 3)
print(input)
output = torch.erf(torch.tensor(input))
print(output)