'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(1, 2)
print('input_data: ', input_data)
output_data = torch.clone(input_data)
print('output_data: ', output_data)
print('input_data is output_data: ', (input_data is output_data))
print('input_data == output_data: ', (input_data == output_data))