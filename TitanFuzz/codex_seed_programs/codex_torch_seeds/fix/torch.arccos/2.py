'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
import numpy as np
input_data = np.array([0.0, 0.5, 1.0])
input_data = torch.from_numpy(input_data)
output = torch.arccos(input_data)
print('Input:', input_data)
print('Output:', output)