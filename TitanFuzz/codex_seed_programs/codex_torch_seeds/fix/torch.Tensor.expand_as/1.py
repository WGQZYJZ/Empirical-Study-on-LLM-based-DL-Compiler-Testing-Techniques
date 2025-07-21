'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand_as\ntorch.Tensor.expand_as(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3, 3)
print('Input tensor: {}'.format(input_tensor))
print('Other tensor: {}'.format(other))
expanded_tensor = torch.Tensor.expand_as(input_tensor, other)
print('Expanded tensor: {}'.format(expanded_tensor))