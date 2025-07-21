'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor: {}'.format(input_tensor))
output_tensor = torch.Tensor.div_(input_tensor, 2)
print('Output Tensor: {}'.format(output_tensor))