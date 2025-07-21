'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
input_data = torch.randn(5, 3)
print('Input data: ', input_data)
output = torch.nn.functional.leaky_relu(input_data)
print('Output: ', output)