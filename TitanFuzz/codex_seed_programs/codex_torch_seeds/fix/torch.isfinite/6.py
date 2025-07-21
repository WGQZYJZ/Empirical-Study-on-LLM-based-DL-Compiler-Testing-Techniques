'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input_data = torch.rand(10, 10)
input_data[0][0] = float('nan')
input_data[0][1] = float('inf')
input_data[0][2] = float('-inf')
output = torch.isfinite(input_data)
print('input_data: \n', input_data)
print('output: \n', output)