'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atanh\ntorch.atanh(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3, 4, 5)
output_data = torch.atanh(input_data)
print('input_data is: \n', input_data)
print('output_data is: \n', output_data)