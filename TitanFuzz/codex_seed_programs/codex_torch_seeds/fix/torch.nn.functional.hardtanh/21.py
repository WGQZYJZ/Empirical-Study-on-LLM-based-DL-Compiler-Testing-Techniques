'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
import numpy as np
input_data = np.random.uniform(low=(- 2), high=2, size=(2, 3))
input_data = torch.from_numpy(input_data)
output_data = torch.nn.functional.hardtanh(input_data, min_val=(- 1.0), max_val=1.0)
print('input_data: ', input_data)
print('output_data: ', output_data)