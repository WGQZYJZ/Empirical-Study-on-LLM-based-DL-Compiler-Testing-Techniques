'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(1, 1, 1, 1, dtype=torch.float32)
torch.polygamma(1, input)
print(torch.polygamma(1, input))
print(type(torch.polygamma(1, input)))