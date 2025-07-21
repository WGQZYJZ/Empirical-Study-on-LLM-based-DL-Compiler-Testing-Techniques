'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(2, 3)
print('Input data:', input_data)
output_data = F.hardtanh(input_data)
print('Output data:', output_data)