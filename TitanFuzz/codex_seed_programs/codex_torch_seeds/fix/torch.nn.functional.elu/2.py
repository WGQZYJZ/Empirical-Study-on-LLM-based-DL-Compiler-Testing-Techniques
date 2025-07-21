'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
input_data = torch.randn(3, 5)
output = torch.nn.functional.elu(input_data)
print('input_data: ', input_data)
print('output: ', output)