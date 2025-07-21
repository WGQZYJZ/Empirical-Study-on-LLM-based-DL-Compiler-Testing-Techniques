'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atanh_\ntorch.Tensor.atanh_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: ', input_tensor)
output_tensor = torch.Tensor.atanh_(input_tensor)
print('Output Tensor: ', output_tensor)