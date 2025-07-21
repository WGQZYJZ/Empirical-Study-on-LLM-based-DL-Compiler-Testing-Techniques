'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq_\ntorch.Tensor.eq_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
output_tensor = torch.Tensor.eq_(input_tensor, other)
print('input_tensor = \n', input_tensor)
print('other = \n', other)
print('output_tensor = \n', output_tensor)