'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
input_data = torch.randn(1, 3)
elu = torch.nn.ELU(alpha=1.0, inplace=False)
output_data = elu(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)