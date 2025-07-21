'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_\ntorch.Tensor.less_(_input_tensor, other)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
'\nTask 3: Call the API torch.Tensor.less_\ntorch.Tensor.less_(_input_tensor, other)\n'
output_tensor = torch.Tensor.less_(input_tensor, other)
print('input_tensor = \n', input_tensor)
print('other = \n', other)
print('output_tensor = \n', output_tensor)