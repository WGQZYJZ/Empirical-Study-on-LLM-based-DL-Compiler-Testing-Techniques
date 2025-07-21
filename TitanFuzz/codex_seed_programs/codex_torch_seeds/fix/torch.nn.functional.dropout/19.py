'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
input_data = torch.randn(10, 16)
output_data = torch.nn.functional.dropout(input_data, p=0.5, training=True)
print('input_data: \n{}'.format(input_data))
print('output_data: \n{}'.format(output_data))