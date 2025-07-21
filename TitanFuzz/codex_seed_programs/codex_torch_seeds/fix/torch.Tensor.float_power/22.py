'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor: ', input_tensor)
tensor_power = torch.Tensor.float_power(input_tensor, 2)
print('Tensor power: ', tensor_power)