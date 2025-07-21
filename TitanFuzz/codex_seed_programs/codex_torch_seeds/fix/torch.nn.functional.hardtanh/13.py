'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
input_data = torch.randn(4, 5)
print('Input data: ', input_data)
output = torch.nn.functional.hardtanh(input_data)
print('Output: ', output)
output = torch.nn.functional.hardtanh(input_data, min_val=0, max_val=1)
print('Output: ', output)