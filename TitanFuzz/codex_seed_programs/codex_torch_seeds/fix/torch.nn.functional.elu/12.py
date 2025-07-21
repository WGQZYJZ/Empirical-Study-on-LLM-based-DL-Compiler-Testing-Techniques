'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
input_data = torch.randn(5, 3)
output_data = torch.nn.functional.elu(input_data)
print('Input data: {}\nOutput data: {}'.format(input_data, output_data))