"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn.functional as F
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
input_data = np.random.rand(1, 1, 6, 6)
input_data = torch.from_numpy(input_data)
print('Input data: ', input_data)
print('Task 3: Call the API torch.nn.functional.upsample')
print('Output data: ', F.upsample(input_data, size=(8, 8), mode='nearest'))