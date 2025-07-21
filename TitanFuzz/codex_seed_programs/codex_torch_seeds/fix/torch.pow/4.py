'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
import numpy as np
input_data = torch.arange(0, 10, dtype=torch.float)
print('input data:', input_data)
print('output data:', torch.pow(input_data, 2))