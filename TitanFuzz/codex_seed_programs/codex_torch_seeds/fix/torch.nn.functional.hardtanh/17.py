'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
import numpy as np
input_data = np.random.randn(1, 3, 3, 3)
input_data = torch.tensor(input_data, dtype=torch.float32)
output = torch.nn.functional.hardtanh(input_data)
print('Input Data = \n', input_data)
print('Output = \n', output)