'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(2, 4)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.divide(input_tensor, 2)
print('output_tensor: ', output_tensor)