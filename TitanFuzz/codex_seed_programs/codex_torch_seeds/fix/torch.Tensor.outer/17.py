'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
input_tensor = torch.arange(1, 5)
vec2 = torch.arange(1, 3)
print('input_tensor: ', input_tensor)
print('vec2: ', vec2)
output_tensor = torch.Tensor.outer(input_tensor, vec2)
print('output_tensor: ', output_tensor)
print('\nResult:')
print('output_tensor: ', output_tensor)