'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
import numpy as np
print('PyTorch version: ', torch.__version__)
input_data = np.random.rand(3, 4).astype(np.float32)
input_data = torch.from_numpy(input_data)
print('Input data: ', input_data)
output_data = torch.special.digamma(input_data)
print('Output data: ', output_data)