'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
import numpy as np
input_data = np.array([[1, 2], [3, 4]])
print('Input data: ', input_data)
output_data = torch.as_tensor(input_data, dtype=None, device=None)
print('Output data: ', output_data)