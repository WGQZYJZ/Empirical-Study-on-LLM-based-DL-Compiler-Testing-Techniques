'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctanh_\ntorch.Tensor.arctanh_(_input_tensor, other)\n'
import torch
tensor_input = torch.randn(4, 4)
print('Input tensor: \n', tensor_input)
tensor_output = torch.Tensor.arctanh_(tensor_input, out=None)
print('Output tensor: \n', tensor_output)