'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsinh_\ntorch.Tensor.arcsinh_(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data is: ', input_data)
output = torch.Tensor.arcsinh_(input_data)
print('Output is: ', output)