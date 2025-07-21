'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.arange(12).reshape(3, 4)
print('Input tensor:')
print(input_tensor)
print('\n')
output_tensor = input_tensor.divide(2)
print('Output tensor:')
print(output_tensor)