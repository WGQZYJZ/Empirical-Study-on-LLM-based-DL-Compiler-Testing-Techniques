'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
input_data = torch.randn(2, 3, 4)
print('Input data: ', input_data)
output_data = torch.flatten(input_data)
print('Output data: ', output_data)