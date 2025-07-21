'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(5, 3, requires_grad=True)
exponent = torch.tensor([2, 3, 4])
output_tensor = input_tensor.float_power(exponent)
print('input_tensor:', input_tensor)
print('exponent:', exponent)
print('output_tensor:', output_tensor)