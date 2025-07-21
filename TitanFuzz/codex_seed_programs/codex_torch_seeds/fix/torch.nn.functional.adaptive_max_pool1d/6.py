'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
import torch
input_data = torch.randn(1, 1, 8)
print('Input data: ', input_data)
output = torch.nn.functional.adaptive_max_pool1d(input_data, 3)
print('Output: ', output)