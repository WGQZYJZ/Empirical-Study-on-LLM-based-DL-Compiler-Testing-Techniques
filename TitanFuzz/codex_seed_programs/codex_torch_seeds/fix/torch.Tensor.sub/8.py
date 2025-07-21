'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
output_tensor = input_tensor.sub(other)
print('output_tensor =\n', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(input, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
input_tensor.sub_(other)
print('input_tensor =\n', input_tensor)