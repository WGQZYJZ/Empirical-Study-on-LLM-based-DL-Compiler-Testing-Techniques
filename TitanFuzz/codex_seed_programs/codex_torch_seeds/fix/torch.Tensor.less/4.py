'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less\ntorch.Tensor.less(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(3, 4)
other = torch.randn(3, 4)
print('Input tensor: {}'.format(input_tensor))
print('Other tensor: {}'.format(other))
output_tensor = input_tensor.less(other)
print('Output tensor: {}'.format(output_tensor))