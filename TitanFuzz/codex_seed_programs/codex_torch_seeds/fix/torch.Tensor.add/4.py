'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
output_tensor = torch.Tensor.add(input_tensor, other)
print('input_tensor: {}'.format(input_tensor))
print('other: {}'.format(other))
print('output_tensor: {}'.format(output_tensor))