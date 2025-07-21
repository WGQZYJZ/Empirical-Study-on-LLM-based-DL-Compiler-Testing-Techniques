'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan_\ntorch.Tensor.arctan_(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: {}'.format(input_data))
output_data = torch.Tensor.arctan_(input_data)
print('Output data: {}'.format(output_data))