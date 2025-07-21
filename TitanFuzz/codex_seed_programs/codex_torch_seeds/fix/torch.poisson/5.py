'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.poisson\ntorch.poisson(input, generator=None)\n'
import torch
import numpy as np
input = torch.rand(10, 10)
output = torch.poisson(input)
print(output)