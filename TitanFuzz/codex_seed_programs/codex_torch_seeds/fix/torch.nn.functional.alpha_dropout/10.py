'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.alpha_dropout\ntorch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
import torch
input_data = torch.randn(1, 3)
print('input_data: ', input_data)
output_data = torch.nn.functional.alpha_dropout(input_data, p=0.5, training=False, inplace=False)
print('output_data: ', output_data)