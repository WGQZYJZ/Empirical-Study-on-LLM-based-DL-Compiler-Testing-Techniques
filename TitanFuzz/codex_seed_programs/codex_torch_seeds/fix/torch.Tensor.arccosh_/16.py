'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh_\ntorch.Tensor.arccosh_(_input_tensor, )\n'
import torch
input_data = torch.randn(8)
print('Input data: ', input_data)
output_data = torch.Tensor.arccosh_(input_data)
print('Output data: ', output_data)