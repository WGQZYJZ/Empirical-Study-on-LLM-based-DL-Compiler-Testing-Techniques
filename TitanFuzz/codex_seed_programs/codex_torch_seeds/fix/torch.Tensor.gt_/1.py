'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gt_\ntorch.Tensor.gt_(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor: \n', input_tensor)
other = torch.rand(2, 3)
print('other: \n', other)
output_tensor = input_tensor.gt_(other)
print('output_tensor: \n', output_tensor)