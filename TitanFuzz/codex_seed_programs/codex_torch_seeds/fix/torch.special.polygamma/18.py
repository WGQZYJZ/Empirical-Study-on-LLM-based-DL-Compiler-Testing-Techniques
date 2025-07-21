'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(2, 3)
n = 5
out = torch.special.polygamma(n, input)
print('The output is:', out)