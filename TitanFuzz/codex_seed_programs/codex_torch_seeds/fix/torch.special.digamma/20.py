'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
import numpy as np
input = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
output = torch.special.digamma(input)
print(output)