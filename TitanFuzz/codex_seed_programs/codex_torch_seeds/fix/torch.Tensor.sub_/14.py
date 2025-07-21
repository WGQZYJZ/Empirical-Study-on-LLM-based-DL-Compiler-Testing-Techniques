'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
print('Input Tensor: ', input_tensor)
print('Other Tensor: ', other)
input_tensor.sub_(other)
print('Output Tensor: ', input_tensor)