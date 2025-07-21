'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
hardtanh = nn.Hardtanh(min_val=(- 1.0), max_val=1.0)
print('The input data: {}'.format(input_data))
print('The output data: {}'.format(hardtanh(input_data)))