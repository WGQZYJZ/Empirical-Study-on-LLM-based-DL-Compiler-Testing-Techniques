'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power_\ntorch.Tensor.float_power_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(2, 3, dtype=torch.float32)
print('Input: ', input_tensor)
exponent = torch.tensor([2, 3, 4])
print('Exponent: ', exponent)
output_tensor = torch.Tensor.float_power_(input_tensor, exponent)
print('Output: ', output_tensor)