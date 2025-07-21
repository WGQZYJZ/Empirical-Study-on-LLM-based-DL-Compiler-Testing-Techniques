'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu6\ntorch.nn.functional.relu6(input, inplace=False)\n'
import torch
input_data = torch.randn(10, 5)
output_data = torch.nn.functional.relu6(input_data)
print('input data: ', input_data)
print('output data: ', output_data)