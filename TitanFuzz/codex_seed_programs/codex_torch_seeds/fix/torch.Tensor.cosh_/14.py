'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cosh_\ntorch.Tensor.cosh_(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
output = torch.Tensor.cosh_(input_data)
print('Output data: ', output)