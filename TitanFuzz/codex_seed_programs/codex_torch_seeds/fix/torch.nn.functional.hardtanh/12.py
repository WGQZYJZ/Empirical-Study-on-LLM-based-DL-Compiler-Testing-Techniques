'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
import torch
input_data = torch.randn(1, 1, 2, 2)
print('Input data: \n', input_data)
output_data = torch.nn.functional.hardtanh(input_data)
print('Output data: \n', output_data)