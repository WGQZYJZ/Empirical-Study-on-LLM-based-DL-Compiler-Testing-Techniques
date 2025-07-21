'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan_\ntorch.Tensor.arctan_(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 5)
print('Input data: ', input_tensor)
output_tensor = torch.Tensor.arctan_(input_tensor)
print('Output data: ', output_tensor)