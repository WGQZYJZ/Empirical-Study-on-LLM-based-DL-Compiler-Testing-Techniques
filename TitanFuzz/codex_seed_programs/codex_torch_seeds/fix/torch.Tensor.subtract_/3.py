'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 2)
other_tensor = torch.rand(3, 2)
print('input_tensor: ', input_tensor)
print('other_tensor: ', other_tensor)
result_tensor = torch.Tensor.subtract_(input_tensor, other_tensor)
print('result_tensor: ', result_tensor)