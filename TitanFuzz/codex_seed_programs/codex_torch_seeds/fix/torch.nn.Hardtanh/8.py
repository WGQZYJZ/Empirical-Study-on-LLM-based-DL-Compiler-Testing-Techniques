'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
import numpy as np
data = np.random.rand(2, 3)
print('Input data: ', data)
input_data = torch.Tensor(data)
print('Tensor: ', input_data)
hardtanh = torch.nn.Hardtanh()
output = hardtanh(input_data)
print('Output: ', output)