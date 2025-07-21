'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool1d\ntorch.nn.functional.adaptive_avg_pool1d(input, output_size)\n'
import torch
import torch
input_data = torch.randn(1, 1, 10)
output_data = torch.nn.functional.adaptive_avg_pool1d(input_data, output_size=5)
print('Input data: \n', input_data)
print('Output data: \n', output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
import torch
input_data = torch.randn(1, 1, 10, 10)