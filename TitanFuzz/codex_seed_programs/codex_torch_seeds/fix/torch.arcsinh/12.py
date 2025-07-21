'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsinh\ntorch.arcsinh(input, *, out=None)\n'
import torch
input_data = torch.arange((- 5), 5, 0.1, dtype=torch.float)
output_data = torch.arcsinh(input_data)
print('Input: \n', input_data)
print('Output: \n', output_data)